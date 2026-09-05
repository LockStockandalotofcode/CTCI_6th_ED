import unittest

# Mathematical 
def diving_board(shorter: int, longer: int, k: int) -> list[int]:
    # direct iteration
    # Time: O(K)
    # Auxiliary Space: O(1), excluding output array

    if k == 0:
        return []

    if shorter == longer:
        return [k * shorter]

    lengths = []
    for freq_longer in range(k + 1):
        freq_shorter = k - freq_longer
        total_length = (freq_shorter * shorter) + (freq_longer * longer)
        lengths.append(total_length)

    return lengths

# =====================================================================
# TEST SUITE
# =====================================================================
class TestDivingBoard(unittest.TestCase):

    def test_01_zero_planks(self):
        """K = 0 returns empty list."""
        self.assertEqual(diving_board(1, 2, 0), [])

    def test_02_equal_length_planks(self):
        """Shorter and longer planks equal length produces 1 unique length."""
        self.assertEqual(diving_board(5, 5, 4), [20])

    def test_03_standard_k_planks(self):
        """Standard distinct planks generate sorted unique lengths."""
        self.assertEqual(diving_board(1, 2, 3), [3, 4, 5, 6])

    def test_04_k_equals_one(self):
        """K = 1 produces shorter and longer directly."""
        self.assertEqual(diving_board(2, 7, 1), [2, 7])

    def test_05_large_k_length_count(self):
        """K = 10 produces exactly K + 1 unique lengths."""
        res = diving_board(3, 5, 10)
        self.assertEqual(len(res), 11)
        self.assertEqual(res, sorted(list(set(res))))


# =====================================================================
# CONCISE SINGLE-LINE TEST RUNNER
# =====================================================================
def run_tests(test_class, title: str):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: {title}\n{'='*75}")

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
            err_msg = result.failures[0][1].strip().splitlines()[-1]
            print(f"  ❌ [FAIL] {desc} | Details: {err_msg}")
            failed += 1
        elif result.errors:
            err_msg = result.errors[0][1].strip().splitlines()[-1]
            print(f"  ⚠️  [ERROR] {desc} | Details: {err_msg}")
            errors += 1

    total = passed + failed + errors
    pass_rate = (passed / total * 100) if total > 0 else 0.0

    print(f"{'-'*75}")
    print(f" SUMMARY: Total: {total} | Passed: {passed} ✅ | Failed: {failed} ❌ | Errors: {errors} ⚠️ | Rate: {pass_rate:.1f}%")
    print(f"{'='*75}\n")


if __name__ == "__main__":
    run_tests(TestDivingBoard, "CTCI 16.11 - Diving Board")