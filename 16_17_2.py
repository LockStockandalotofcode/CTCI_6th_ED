def contiguous_sequence(arr: list[int]) -> bool:
    if not arr:
        return 0

    s = len(arr)
    # KADANE's algorithm starting at very first 
    # O(1) no extra memory single pass
    # running sum decides to start it at current num or keep the running sum 
    max_sum = arr[0]
    curr_sum = arr[0]
    for num in arr[1: ]:
        curr_sum = max(curr_sum + num, num)
        max_sum = max(max_sum, curr_sum)

    return max_sum

import unittest

# =====================================================================
# SOLUTION PLACEHOLDER
# Replace or import your actual function here
# =====================================================================
# def contiguous_sequence(arr: list[int]) -> int:
#     """Calculates the maximum contiguous subarray sum (Kadane's Algorithm)."""
#     if not arr:
#         return 0
#     max_sum = arr[0]
#     current_sum = arr[0]
#     for num in arr[1:]:
#         current_sum = max(num, current_sum + num)
#         max_sum = max(max_sum, current_sum)
#     return max_sum


# =====================================================================
# TEST SUITE
# =====================================================================
class TestContiguousSequence(unittest.TestCase):

    def test_01_empty_array(self):
        """Empty array should return 0 (sum of empty subarray)."""
        self.assertEqual(contiguous_sequence([]), 0)

    def test_02_single_element_positive(self):
        """Single positive element returns its own value."""
        self.assertEqual(contiguous_sequence([5]), 5)

    def test_03_single_element_negative(self):
        """Single negative element returns its own value."""
        self.assertEqual(contiguous_sequence([-7]), -7)

    def test_04_single_element_zero(self):
        """Single zero element returns 0."""
        self.assertEqual(contiguous_sequence([0]), 0)

    def test_05_all_positive_numbers(self):
        """All positive numbers should sum the entire array."""
        self.assertEqual(contiguous_sequence([1, 2, 3, 4, 5]), 15)

    def test_06_all_negative_numbers(self):
        """All negative numbers should return the least negative single element."""
        self.assertEqual(contiguous_sequence([-5, -2, -8, -1, -4]), -1)

    def test_07_all_zeros(self):
        """Array of all zeros returns 0."""
        self.assertEqual(contiguous_sequence([0, 0, 0, 0]), 0)

    def test_08_ctci_classic_example(self):
        """CTCI example: [2, -8, 3, -2, 4, -10] -> Max sum is 5."""
        self.assertEqual(contiguous_sequence([2, -8, 3, -2, 4, -10]), 5)

    def test_09_subarray_at_start(self):
        """Maximum subarray is located at the start of the array."""
        self.assertEqual(contiguous_sequence([10, 20, -30, 5, 2]), 30)

    def test_10_subarray_at_end(self):
        """Maximum subarray is located at the end of the array."""
        self.assertEqual(contiguous_sequence([-50, -10, 15, 25]), 40)

    def test_11_entire_array_is_max(self):
        """Entire array with small negative drops gives max sum."""
        self.assertEqual(contiguous_sequence([3, -1, 4, -1, 5]), 10)

    def test_12_large_negative_separator(self):
        """Large negative separator splits array into isolated positive choices."""
        self.assertEqual(contiguous_sequence([100, -1000, 200]), 200)

    def test_13_alternating_signs(self):
        """Alternating positive and negative sequence."""
        self.assertEqual(contiguous_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)


# =====================================================================
# INFORMATIVE TEST RUNNER
# =====================================================================
def run_informative_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.17 - Contiguous Sequence\n{'='*75}")

    passed, failed, errors = 0, 0, 0
    failures_details = []

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
            for _, err in result.failures:
                failures_details.append((test_name, doc, err))
        elif result.errors:
            print(f"  ⚠️  [ERROR] {desc}")
            errors += 1
            for _, err in result.errors:
                failures_details.append((test_name, doc, err))

    total = passed + failed + errors
    pass_rate = (passed / total * 100) if total > 0 else 0.0

    print(f"\n{'-'*75}")
    print(f" EXECUTION SUMMARY:")
    print(f" Total Tests : {total}")
    print(f" Passed      : {passed} ✅")
    print(f" Failed      : {failed} ❌")
    print(f" Errors      : {errors} ⚠️")
    print(f" Success Rate: {pass_rate:.1f}%")
    print(f"{'='*75}\n")

    # if failures_details:
    #     print(f"{'!'*75}\n DETAILED FAILURE / ERROR REPORT:\n{'!'*75}")
    #     for name, doc, err in failures_details:
    #         print(f"• Test: {name}\n  Description: {doc}\n  Traceback:\n{err}\n{'-'*75}")


if __name__ == "__main__":
    run_informative_tests(TestContiguousSequence)