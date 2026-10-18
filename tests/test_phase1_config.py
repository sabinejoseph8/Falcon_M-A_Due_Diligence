"""Phase 1: the agents, commands, guardrails and lead-agent instructions are set up correctly."""
import json
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

    def test_reading_the_answer_key_needs_approval(self):
        self.assertIn("Read(/evaluation/answer-key.md)", self.permissions.get("ask", []))

    def test_reading_earlier_runs_needs_approval(self):
        for rule in ("Read(/examples/**)", "Read(/runs/**)"):
            self.assertIn(rule, self.permissions.get("ask", []))


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


if __name__ == "__main__":
    unittest.main()
