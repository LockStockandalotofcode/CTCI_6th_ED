import unittest

def sub_sort(arr:list[int]) -> tuple[int, int]:
    # early return empty/edge case
    if not arr or len(arr) < 2:
        return (-1, -1)

    # STEP 1
    # find end of left sorted subsequence
    end_left = 0
    while end_left < len(arr) - 1 and arr[end_left] < arr[end_left + 1]:
        end_left += 1
    # early return 2
    if end_left == len(arr) - 1:
        return (-1, -1)

    # find start of right sorted subsequence
    start_right = len(arr) - 1
    while start_right > 0 and arr[start_right] >= arr[start_right - 1]:
        start_right -= 1

    # STEP 2
    # find min and max in the middle unsorted subarray
    min_mid = min(arr[end_left : start_right + 1])
    max_mid = max(arr[end_left : start_right + 1])

    # STEP 3
    # Shrink left segment until you come across element <= min_mid
    left_idx = end_left
    while left_idx >= 0 and arr[left_idx] > min_mid:
        left_idx -= 1
    mid_start = left_idx + 1

    # Shrink right segment until you come across element >= max_mid
    right_idx = start_right
    while right_idx < len(arr) and arr[right_idx] < max_mid:
        right_idx += 1
    mid_end = right_idx - 1
    
    return (mid_start, mid_end)
    


    
    

    
# # =====================================================================
# # SOLUTION PLACEHOLDER
# # Replace or import your actual function here
# # =====================================================================
# def sub_sort(arr: list[int]) -> tuple[int, int]:
#     """Finds indices m and n such that sorting arr[m:n+1] sorts the entire array.
#     Returns (-1, -1) if the array is already sorted or has fewer than 2 elements.
#     """
#     if len(arr) < 2:
#         return (-1, -1)

#     left_end = 0
#     while left_end < len(arr) - 1 and arr[left_end] <= arr[left_end + 1]:
#         left_end += 1

#     if left_end == len(arr) - 1:
#         return (-1, -1)

#     right_end = len(arr) - 1
#     while right_end > 0 and arr[right_end] >= arr[right_end - 1]:
#         right_end -= 1

#     min_mid = min(arr[left_end : right_end + 1])
#     max_mid = max(arr[left_end : right_end + 1])

#     m = left_end
#     while m > 0 and arr[m - 1] > min_mid:
#         m -= 1

#     n = right_end
#     while n < len(arr) - 1 and arr[n + 1] < max_mid:
#         n += 1

#     return (m, n)


# =====================================================================
# TEST SUITE
# =====================================================================
class TestSubSort(unittest.TestCase):

    def test_01_empty_and_single_element(self):
        """Empty or single-element array returns (-1, -1)."""
        self.assertEqual(sub_sort([]), (-1, -1))
        self.assertEqual(sub_sort([42]), (-1, -1))

    def test_02_already_sorted(self):
        """Already sorted array returns (-1, -1)."""
        self.assertEqual(sub_sort([1, 2, 3, 4, 5, 6]), (-1, -1))

    def test_03_ctci_example(self):
        """CTCI example array [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19] -> (3, 9)."""
        arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        self.assertEqual(sub_sort(arr), (3, 9))

    def test_04_completely_reversed(self):
        """Reversed array requires sorting entire range from 0 to N-1."""
        self.assertEqual(sub_sort([5, 4, 3, 2, 1]), (0, 4))

    def test_05_duplicates_and_flat_regions(self):
        """Array with duplicate values requiring middle boundary adjustment."""
        self.assertEqual(sub_sort([1, 2, 4, 4, 3, 5]), (2, 4))

    def test_06_single_swap_needed(self):
        """Only two adjacent elements out of order."""
        self.assertEqual(sub_sort([1, 3, 2, 4]), (1, 2))


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.16 - Sub Sort\n{'='*75}")

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
    run_tests(TestSubSort)