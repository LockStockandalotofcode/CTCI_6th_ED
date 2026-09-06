import unittest

def _sum_range(start: int, end: int) -> int:
    # helper: calculate sum of range both start, end inclusive
    count = end - start + 1
    return count * (start + end) // 2

def find_missing_two(nums: list[int]) -> tuple[int, int]:
    # Pivot splitting via average threshold
    # TIme: O(N)
    # Space: O(1)
    n = len(nums) + 2

    expected_sum = _sum_range(0, n)
    actual_sum = sum(nums)

    #  sum_diff = x + y
    sum_diff = expected_sum - actual_sum
    # P pivot
    pivot = sum_diff // 2

    # find smaller missing number first from range [0, P]
    expected_left_sum = _sum_range(0, pivot)
    actual_left_sum  = sum(x for x in nums if x <= pivot)
    x = expected_left_sum - actual_left_sum

    # find larger missing number first from range [P + 1, n]
    expected_right_sum = _sum_range(pivot + 1, n)
    actual_right_sum  = sum(x for x in nums if x > pivot)
    y = expected_right_sum - actual_right_sum

    return (x, y)
    
# =====================================================================
# TEST SUITE
# =====================================================================
class TestMissingTwo(unittest.TestCase):

    def test_01_n_equals_two_empty_array(self):
        """N = 2 with empty array returns (1, 2)."""
        self.assertEqual(find_missing_two([]), (1, 2))

    def test_02_missing_first_and_last(self):
        """Missing boundary elements 1 and N."""
        self.assertEqual(find_missing_two([2, 3, 4]), (1, 5))

    def test_03_missing_adjacent_numbers(self):
        """Missing adjacent internal numbers."""
        self.assertEqual(find_missing_two([1, 2, 5, 6]), (3, 4))

    def test_04_missing_non_adjacent_numbers(self):
        """Missing non-adjacent numbers inside range."""
        self.assertEqual(find_missing_two([1, 3, 5, 7, 6, 8]), (2, 4))

    def test_05_unordered_input_array(self):
        """Handles unordered input array correctly."""
        self.assertEqual(find_missing_two([6, 1, 4, 2]), (3, 5))


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.19 - Missing Two\n{'='*75}")

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
    run_tests(TestMissingTwo)