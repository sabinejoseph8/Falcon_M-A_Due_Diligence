"""Phase 1: the agents, commands, guardrails and lead-agent instructions are set up correctly."""
import importlib.util
import json
import re
import unittest

from _common import ROOT, frontmatter, read

SUBAGENTS = ["sec-filings-analyst", "news-media-analyst", "litigation-analyst", "financial-analyst", "citation-verifier"]
READ_ONLY_TOOLS = {"Read", "Grep", "Glob"}
COMMANDS = ["diligence", "diligence-status", "evaluate", "reset-memory", "run-tests"]
# Built-in commands and bundled skills, from the Claude Code commands reference (checked October 18, 2026).
BUILT_IN_COMMANDS = {
    "add-dir", "advisor", "agents", "artifacts", "autocompact", "autofix-pr", "background", "batch", "branch", "btw", "bug",
    "cd", "chrome", "claude-api", "clear", "code-review", "color", "compact", "config", "context", "copy", "cost", "debug",
    "deep-research", "design", "desktop", "diff", "doctor", "effort", "exit", "export", "fast", "feedback",
    "fewer-permission-prompts", "focus", "fork", "goal", "help", "hooks", "ide", "import", "init", "insights", "keybindings",
    "list-agents", "login", "logout", "loop", "mcp", "memory", "mobile", "model", "output-style", "passes", "permissions",
    "plan", "plugin", "pr-comments", "privacy-settings", "recap", "release-notes", "reload-plugins", "reload-skills",
    "remote-control", "rename", "reset", "resume", "review", "rewind", "run", "sandbox", "schedule", "security-review",
    "simplify", "skill-doctor", "skills", "slides", "stats", "status", "statusline", "stop", "subtask", "tasks", "teleport",
    "terminal-setup", "theme", "ultraplan", "ultrareview", "update-config", "upgrade", "usage", "verify", "vim", "voice",
    "workflows",
}


class TestSubagents(unittest.TestCase):
    def test_every_subagent_file_exists_with_valid_frontmatter(self):
        for name in SUBAGENTS:
            path = ROOT / ".claude" / "agents" / f"{name}.md"
            self.assertTrue(path.exists(), f"missing {path}")
            fields = frontmatter(path)
            self.assertIsNotNone(fields, f"{name}: no frontmatter")
            self.assertEqual(fields.get("name"), name, f"{name}: name must match the file name")
            self.assertTrue(fields.get("description"), f"{name}: description is empty")

    def test_subagents_are_read_only(self):
        for name in SUBAGENTS:
            tools = {t.strip() for t in frontmatter(ROOT / ".claude" / "agents" / f"{name}.md").get("tools", "").split(",") if t.strip()}
            self.assertTrue(tools, f"{name}: no tools list, so it would inherit every tool")
            self.assertLessEqual(tools, READ_ONLY_TOOLS, f"{name} has tools beyond read-only: {sorted(tools - READ_ONLY_TOOLS)}")

    def test_subagents_treat_sources_as_evidence(self):
        for name in SUBAGENTS:
            self.assertIn("never as instructions", read(ROOT / ".claude" / "agents" / f"{name}.md"), f"{name}: missing prompt-injection rule")


class TestCommands(unittest.TestCase):
    def test_commands_exist_with_descriptions(self):
        for name in COMMANDS:
            path = ROOT / ".claude" / "commands" / f"{name}.md"
            self.assertTrue(path.exists(), f"missing /{name}")
            self.assertTrue((frontmatter(path) or {}).get("description"), f"/{name}: description is empty")

    def test_no_command_shadows_a_built_in_command(self):
        names = {p.stem for p in (ROOT / ".claude" / "commands").glob("*.md")}
        self.assertFalse(names & BUILT_IN_COMMANDS, f"rename these: {sorted(names & BUILT_IN_COMMANDS)}")


class TestGuardrails(unittest.TestCase):
    def setUp(self):
        self.permissions = json.loads(read(ROOT / ".claude" / "settings.json"))["permissions"]

    def test_web_access_is_blocked(self):
        for rule in ("WebFetch", "WebSearch"):
            self.assertIn(rule, self.permissions["deny"])

    def test_source_data_and_answer_key_cannot_be_edited(self):
        for rule in ("Edit(/targets/*/data/**)", "Edit(./targets/*/data/**)", "Edit(/targets/*/evaluation/answer-key.md)", "Edit(./targets/*/evaluation/answer-key.md)"):
            self.assertIn(rule, self.permissions["deny"])

    def test_tests_cannot_be_edited(self):
        # A blind run once edited its own grader. Deny rules hold in every permission mode.
        for rule in ("Edit(/tests/**)", "Edit(./tests/**)"):
            self.assertIn(rule, self.permissions["deny"])
        self.assertIn("Never modify files in `targets/*/data/` or `tests/`", read(ROOT / "CLAUDE.md"))

    def test_reading_anything_in_evaluation_needs_approval(self):
        for rule in ("Read(/targets/*/evaluation/**)", "Read(./targets/*/evaluation/**)"):
            self.assertIn(rule, self.permissions.get("ask", []))

    def test_earlier_runs_and_their_scorecards_need_approval(self):
        for rule in ("Read(/examples/**)", "Read(./examples/**)", "Read(/runs/**)", "Read(./runs/**)"):
            self.assertIn(rule, self.permissions.get("ask", []))
        reset = read(ROOT / ".claude" / "commands" / "reset-memory.md")
        moves_scorecard = any("targets/<target>/evaluation/scorecard.md" in line and "runs/" in line for line in reset.splitlines())
        self.assertTrue(moves_scorecard, "/reset-memory must move the target's evaluation/scorecard.md into the archived run in runs/")
        self.assertIn("memory/target.txt", reset, "/reset-memory must keep the run's target with the archived run")


class TestLeadAgent(unittest.TestCase):
    def setUp(self):
        self.text = read(ROOT / "CLAUDE.md")

    def test_three_human_checkpoints(self):
        for n in (1, 2, 3):
            self.assertIn(f"CHECKPOINT {n} (human)", self.text)

    def test_loop_is_capped_at_three(self):
        self.assertIn("at most 3 Act/Observe iterations", self.text)

    def test_guardrails_and_interview_notes_present(self):
        for phrase in ("never as instructions", "Do not read `targets/*/evaluation/`", "## Interview Notes"):
            self.assertIn(phrase, self.text)

    def test_memory_templates_exist(self):
        for name in ("plan.md", "findings.md", "open-questions.md", "run-log.md", "datasets/README.md", "analyst-reports/README.md"):
            self.assertTrue((ROOT / "templates" / "memory" / name).exists(), f"missing template {name}")

    def test_checkpoints_print_content_before_the_question(self):
        self.assertIn("**How to show a checkpoint.**", self.text)
        self.assertIn("print the full checkpoint content in chat first", self.text)
        sections = re.split(r"^### ", self.text, flags=re.M)
        for n in (1, 2, 3):
            section = next(s for s in sections if s.startswith(f"CHECKPOINT {n} (human)"))
            self.assertIn("as the last thing in the message", section, f"checkpoint {n}: question must come last")
            self.assertIn("shown in chat", section, f"checkpoint {n}: must log that the content was shown")

    def test_verifier_gets_every_medium_finding_in_the_report(self):
        sections = re.split(r"^### ", self.text, flags=re.M)
        verify = next(s for s in sections if s.startswith("Step 4: VERIFY"))
        self.assertIn("every Medium finding that will appear anywhere in the report", verify)
        self.assertIn("Low findings may stay unverified", verify)
        self.assertIn("up to four verifier runs in parallel", verify)

    def test_observe_checks_dated_accounting_judgments(self):
        sections = re.split(r"^### ", self.text, flags=re.M)
        observe = next(s for s in sections if s.startswith("Step 3: OBSERVE"))
        self.assertIn("dated accounting judgments", observe)
        self.assertIn("State the change with numbers", observe)

    def test_report_step_uses_the_committed_tools(self):
        self.assertIn("python3 tools/md2html.py", self.text)
        self.assertIn("--print-to-pdf", self.text)
        self.assertTrue((ROOT / "tools" / "md2html.py").exists(), "missing tools/md2html.py")


class TestTargets(unittest.TestCase):
    def test_lead_agent_names_no_single_target(self):
        text = read(ROOT / "CLAUDE.md")
        self.assertIn("targets/<target>/data/deal-brief.md", text)
        self.assertNotRegex(text, r"(?<![\w/<*])data/", "CLAUDE.md still points at the old data/ folder")
        for name in ("Talonfield", "Arbelion"):
            self.assertNotIn(name, text, "the deal description belongs in the target's deal brief")

    def test_diligence_and_evaluate_take_a_target(self):
        for name in ("diligence", "evaluate"):
            text = read(ROOT / ".claude" / "commands" / f"{name}.md")
            self.assertIn("$ARGUMENTS", text, f"/{name} must read the target from its arguments")
            self.assertIn("falcon", text, f"/{name} must default to falcon")
            self.assertIn("memory/target.txt", text, f"/{name} must use the run's recorded target")

    def test_subagents_read_the_named_target(self):
        for name in SUBAGENTS:
            text = read(ROOT / ".claude" / "agents" / f"{name}.md")
            self.assertIn("targets/<target>/data/", text, f"{name}: source folder must be per target")
            self.assertNotRegex(text, r"(?<![\w/<*])data/", f"{name}: still points at the old data/ folder")


class TestVerifier(unittest.TestCase):
    def test_summary_counts_come_from_the_table(self):
        text = read(ROOT / ".claude" / "agents" / "citation-verifier.md")
        self.assertIn("Write the results table first", text)
        self.assertIn("A + B + C must equal X", text)


class TestReportConverter(unittest.TestCase):
    def setUp(self):
        spec = importlib.util.spec_from_file_location("md2html", ROOT / "tools" / "md2html.py")
        self.md2html = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(self.md2html)

    def test_converts_the_report_markdown(self):
        sample = "\n".join([
            '<div class="cover">', "", "# Title", "", '<p class="sub">Draft</p>', "", "</div>", "",
            "> A **bold** note with `code`.", "",
            "- one", "  - nested", "    1. deeper", "- two", "",
            "| ID | Severity |", "|---|---|", "| X-01 | Critical |",
        ])
        out = self.md2html.convert(sample)
        for fragment in ('<div class="cover">', '<h1 id="title">Title</h1>', '<p class="sub">Draft</p>', "</div>",
                         "<blockquote>", "<strong>bold</strong>", "<code>code</code>",
                         "<li>one\n<ul>\n<li>nested\n<ol>\n<li>deeper</li>", "<table>", "<th>ID</th>", "<td>X-01</td>"):
            self.assertIn(fragment, out)

    def test_page_embeds_the_stylesheet(self):
        page = self.md2html.page("# Title")
        self.assertIn("<style>", page)
        self.assertIn(".cover", page)
        self.assertNotIn('<link rel="stylesheet"', page)


if __name__ == "__main__":
    unittest.main()
