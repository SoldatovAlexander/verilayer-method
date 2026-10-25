import copy
import json
import unittest
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from check_gate import decide

FIXTURES = Path(__file__).resolve().parents[1] / ".verilayer" / "fixtures"


def load(name):
    return json.loads((FIXTURES / (name + ".json")).read_text(encoding="utf-8"))


class GateFixtureTests(unittest.TestCase):
    def test_approved_passes(self):
        self.assertEqual(decide(load("pass-verified"))["gate"], "PASS")

    def test_missing_verification_blocks(self):
        self.assertEqual(decide(load("block-not-run"))["gate"], "BLOCKED")

    def test_stale_evidence_blocks(self):
        self.assertEqual(decide(load("block-stale-evidence"))["gate"], "BLOCKED")

    def test_parallel_safe_action_proceeds(self):
        self.assertEqual(decide(load("pass-independent-work"))["gate"], "PASS")

    def test_waived_is_not_verified(self):
        record = load("pass-verified")
        record["verification_obligations"][0]["status"] = "WAIVED"
        self.assertEqual(decide(record)["gate"], "BLOCKED")

    def test_missing_provenance_blocks(self):
        record = load("pass-verified")
        record["evidence"][0]["source_ref"] = ""
        self.assertEqual(decide(record)["gate"], "BLOCKED")

    def test_wrong_claim_scope_blocks(self):
        record = load("pass-verified")
        record["verification_obligations"][0]["scope"] = "unrelated"
        self.assertEqual(decide(record)["gate"], "BLOCKED")

    def test_duplicate_obligations_are_invalid(self):
        record = load("pass-verified")
        record["verification_obligations"].append(copy.deepcopy(record["verification_obligations"][0]))
        with self.assertRaises(ValueError):
            decide(record)


if __name__ == "__main__":
    unittest.main()
