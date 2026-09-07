import unittest
from collections import Counter

def _get_color_index(char: str) -> int:
    # helper meps color character to array index 
    mapping = {"R": 0, "G": 1, "B": 2, "Y": 3}
    return mapping.get(char, -1)

def master_mind(guess: str, solution: str) -> tuple[int, int]:
    # 2-pass frequency array matching
    # time: O(1)
    # Space: O(1)
    if len(solution) != len(guess) or len(solution) != 4:
        return 0, 0

    hits = 0
    pseudo_hits = 0

    solution_freq = [0] * 4
    guess_freq = [0] * 4

    # pass 1: count exact hits and record non-matching freqs
    for i in range(len(solution)):
        if solution[i] == guess[i]:
            hits += 1
        else:
            s_idx = _get_color_index(solution[i])
            g_idx = _get_color_index(guess[i])
            if s_idx != -1:
                solution_freq[s_idx] += 1
            if g_idx != -1:
                guess_freq[g_idx] += 1

    # pass 2: calculate pseudo-hits using frequency intersection
    for i in range(4):
        pseudo_hits += min(solution_freq[i], guess_freq[i])

    return hits, pseudo_hits


# =====================================================================
# TEST SUITE
# =====================================================================
class TestMasterMind(unittest.TestCase):

    def test_01_all_hits(self):
        """Identical guess and solution return 4 hits and 0 pseudo-hits."""
        self.assertEqual(master_mind("RGBY", "RGBY"), (4, 0))

    def test_02_all_pseudo_hits(self):
        """All colors present in wrong positions return 0 hits and 4 pseudo-hits."""
        self.assertEqual(master_mind("YBGR", "RGBY"), (0, 4))

    def test_03_zero_matches(self):
        """Completely disjoint colors return (0, 0)."""
        self.assertEqual(master_mind("RRRR", "GGGG"), (0, 0))

    def test_04_mixed_hits_and_pseudo_hits(self):
        """Calculates correct combination of hits and pseudo-hits."""
        self.assertEqual(master_mind("GGRR", "RGBY"), (1, 1))

    def test_05_duplicate_color_overcounting_prevention(self):
        """Prevents overcounting duplicate colors in guess beyond solution frequency."""
        self.assertEqual(master_mind("RRRR", "RGBR"), (2, 0))


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.15 - Master Mind\n{'='*75}")

    passed, failed, errors = 0, 0, 0

    for test in suite:
        test_name = test._testMethodName
        doc = (test._testMethodDoc or "").strip()
        desc = f"{test_name} -> {doc}" if doc else test_name

        result = unittest.TestResult()
        test.run(result)

        if result.wasSuccessful():
            print(f"  ✅ [PASS] {desc}")
            passed += 1
        elif result.failures:
            fail_msg = result.failures[0][1].strip().split("\n")[-1]
            print(f"  ❌ [FAIL] {desc} | {fail_msg}")
            failed += 1
        elif result.errors:
            err_msg = result.errors[0][1].strip().split("\n")[-1]
            print(f"  ⚠️  [ERROR] {desc} | {err_msg}")
            errors += 1

    total = passed + failed + errors
    pass_rate = (passed / total * 100) if total > 0 else 0.0

    print(f"\n{'-'*75}")
    print(
        f" SUMMARY: Total: {total} | Passed: {passed} ✅ | Failed: {failed} ❌ | Errors: {errors} ⚠️ | Rate: {pass_rate:.1f}%"
    )
    print(f"{'='*75}\n")


if __name__ == "__main__":
    run_tests(TestMasterMind)