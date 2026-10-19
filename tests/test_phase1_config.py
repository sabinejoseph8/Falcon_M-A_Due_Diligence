"""Phase 1: the agents, commands, guardrails and lead-agent instructions are set up correctly."""
import importlib.util
import json
import re
import unittest

from _common import ROOT, frontmatter, read

SUBAGENTS = ["sec-filings-analyst", "news-media-analyst", "litigation-analyst", "financial-analyst", "citation-verifier"]
READ_ONLY_TOOLS = {"Read", "Grep", "Glob"}
COMMANDS = ["diligence", "diligence-status", "evaluate", "reset-memory", "run-tests"]
BUILT_IN_COMMANDS = {"status", "help", "clear", "reset", "config", "agents", "memory", "init", "model", "cost", "compact", "doctor", "review", "permissions", "resume", "context", "exit", "mcp", "hooks", "plugin"}


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
        for rule in ("Edit(/data/**)", "Edit(./data/**)", "Edit(/evaluation/answer-key.md)", "Edit(./evaluation/answer-key.md)"):
            self.assertIn(rule, self.permissions["deny"])

    def test_reading_anything_in_evaluation_needs_approval(self):
        for rule in ("Read(/evaluation/**)", "Read(./evaluation/**)"):
            self.assertIn(rule, self.permissions.get("ask", []))

    def test_earlier_runs_and_their_scorecards_need_approval(self):
        for rule in ("Read(/examples/**)", "Read(/runs/**)"):
            self.assertIn(rule, self.permissions.get("ask", []))
        reset = read(ROOT / ".claude" / "commands" / "reset-memory.md")
        moves_scorecard = any("evaluation/scorecard.md" in line and "runs/" in line for line in reset.splitlines())
        self.assertTrue(moves_scorecard, "/reset-memory must move evaluation/scorecard.md into the archived run in runs/")


class TestLeadAgent(unittest.TestCase):
    def setUp(self):
        self.text = read(ROOT / "CLAUDE.md")

    def test_three_human_checkpoints(self):
        for n in (1, 2, 3):
            self.assertIn(f"CHECKPOINT {n} (human)", self.text)

    def test_loop_is_capped_at_three(self):
        self.assertIn("at most 3 Act/Observe iterations", self.text)

    def test_guardrails_and_interview_notes_present(self):
        for phrase in ("never as instructions", "Do not read `evaluation/`", "## Interview Notes"):
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

    def test_report_step_uses_the_committed_tools(self):
        self.assertIn("python3 tools/md2html.py", self.text)
        self.assertIn("--print-to-pdf", self.text)
        self.assertTrue((ROOT / "tools" / "md2html.py").exists(), "missing tools/md2html.py")


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
