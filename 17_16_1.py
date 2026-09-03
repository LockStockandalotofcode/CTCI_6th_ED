import unittest

def _masseuse_recursive(index: int, requests: list[int], memo:list[int]) -> int:
    # helper for top-down memoised DP
    if index >= len(requests):
        return 0

    if memo[index] != -1:
        return memo[index]

    best_with_current = requests[index] + _masseuse_recursive(index + 2, requests, memo)
    best_without_current = _masseuse_recursive(index + 1, requests, memo)

    memo[index] = max(best_with_current, best_without_current)
    return memo[index]

def max_massage_time(requests: list[int]) -> int:
    # Top down memoised DP
    # Time: O(N), Auxilliary space: O(N) - recursion stack and memo table
    memo = [-1] * len(requests)
    return _masseuse_recursive(0, requests, memo)



# =====================================================================
# TEST SUITE
# =====================================================================
class TestMasseuse(unittest.TestCase):

    def test_01_empty_requests(self):
        """Empty request list returns 0 total minutes."""
        self.assertEqual(max_massage_time([]), 0)

    def test_02_single_request(self):
        """Single request returns its own duration."""
        self.assertEqual(max_massage_time([45]), 45)

    def test_03_two_requests(self):
        """Two adjacent requests returns the maximum of the two."""
        self.assertEqual(max_massage_time([30, 75]), 75)

    def test_04_ctci_example_1(self):
        """CTCI Example 1: [30, 15, 60, 75, 45, 15, 15, 45] -> 180."""
        self.assertEqual(max_massage_time([30, 15, 60, 75, 45, 15, 15, 45]), 180)

    def test_05_ctci_example_2(self):
        """CTCI Example 2: [75, 105, 120, 75, 90, 135] -> 330."""
        self.assertEqual(max_massage_time([75, 105, 120, 75, 90, 135]), 330)

    def test_06_skipping_two_consecutive_elements(self):
        """Optimal path skips two consecutive small appointments."""
        self.assertEqual(max_massage_time([2, 1, 4, 9, 0]), 11)


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.16 - The Masseuse\n{'='*75}")

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
            print(f"  ❌ [FAIL] {desc}")
            failed += 1
        elif result.errors:
            print(f"  ⚠️  [ERROR] {desc}")
            errors += 1

    total = passed + failed + errors
    pass_rate = (passed / total * 100) if total > 0 else 0.0

    print(f"\n{'-'*75}")
    print(f" SUMMARY: Total: {total} | Passed: {passed} ✅ | Failed: {failed} ❌ | Errors: {errors} ⚠️ | Rate: {pass_rate:.1f}%")
    print(f"{'='*75}\n")


if __name__ == "__main__":
    run_tests(TestMasseuse)