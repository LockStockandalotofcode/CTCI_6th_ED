import heapq
import unittest

def smallest_k(arr: list[int], k: int) -> list[int]:
    #  approach 1 - slide a winodw of size k through array, replacing the max element in window with the smaller element
    if k < 0 or  k > len(arr):
        raise ValueError("k must be between 0 and len(arr)")
    if k == 0:
        return []
    window = arr[:k]
    window.sort()
    for i in range(k, len(arr)):
        if arr[i] < window[-1]:
            window[-1] = arr[i]
            window.sort()

    return window

# # =====================================================================
# # SOLUTION PLACEHOLDER
# # Replace or import your actual function here
# # =====================================================================
# def smallest_k(arr: list[int], k: int) -> list[int]:
#     """Finds the smallest k numbers in an array (Max-Heap approach)."""
#     if k < 0 or k > len(arr):
#         raise ValueError("k must be between 0 and len(arr).")
#     if k == 0 or not arr:
#         return []

#     # Max-heap storing negated values to keep size k
#     max_heap = []
#     for x in arr:
#         heapq.heappush(max_heap, -x)
#         if len(max_heap) > k:
#             heapq.heappop(max_heap)

#     return [-x for x in max_heap]


# =====================================================================
# TEST SUITE
# =====================================================================
class TestSmallestK(unittest.TestCase):

    def test_01_k_equals_zero(self):
        """k = 0 returns empty list."""
        self.assertEqual(smallest_k([1, 2, 3, 4], 0), [])

    def test_02_k_greater_than_length_raises(self):
        """k > len(arr) raises ValueError."""
        with self.assertRaises(ValueError):
            smallest_k([1, 2, 3], 5)

    def test_03_negative_k_raises(self):
        """Negative k raises ValueError."""
        with self.assertRaises(ValueError):
            smallest_k([1, 2, 3], -1)

    def test_04_empty_array_with_k_zero(self):
        """Empty array with k = 0 returns empty list."""
        self.assertEqual(smallest_k([], 0), [])

    def test_05_k_equals_array_length(self):
        """k = len(arr) returns all elements."""
        arr = [5, 3, 1, 4, 2]
        result = smallest_k(arr, 5)
        self.assertEqual(sorted(result), [1, 2, 3, 4, 5])

    def test_06_general_case_unsorted_array(self):
        """General unsorted array case."""
        arr = [1, 5, 2, 9, -1, 10, 0]
        result = smallest_k(arr, 3)
        self.assertEqual(sorted(result), [-1, 0, 1])

    def test_07_array_with_duplicates(self):
        """Array containing duplicate elements."""
        arr = [5, 1, 5, 2, 1, 3]
        result = smallest_k(arr, 3)
        self.assertEqual(sorted(result), [1, 1, 2])

    def test_08_already_sorted_array(self):
        """Already sorted array."""
        arr = [1, 2, 3, 4, 5]
        result = smallest_k(arr, 2)
        self.assertEqual(sorted(result), [1, 2])

    def test_09_reverse_sorted_array(self):
        """Reverse sorted array."""
        arr = [5, 4, 3, 2, 1]
        result = smallest_k(arr, 2)
        self.assertEqual(sorted(result), [1, 2])

    def test_10_single_element_array(self):
        """Single element array with k = 1."""
        self.assertEqual(smallest_k([42], 1), [42])


# =====================================================================
# INFORMATIVE TEST RUNNER
# =====================================================================
def run_informative_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.14 - Smallest K\n{'='*75}")

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

    if failures_details:
        print(f"{'!'*75}\n DETAILED FAILURE / ERROR REPORT:\n{'!'*75}")
        for name, doc, err in failures_details:
            print(f"• Test: {name}\n  Description: {doc}\n  Traceback:\n{err}\n{'-'*75}")


if __name__ == "__main__":
    run_informative_tests(TestSmallestK)