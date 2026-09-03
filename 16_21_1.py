import unittest
from typing import Optional, Tuple

# 2 solutions 

def _compute_target_difference(arr_a: list[int], arr_b: list[int]) -> Optional[int]:
    # helper 
    sum_a, sum_b = sum(arr_a), sum(arr_b)
    diff = sum_a - sum_b

    # target difference must be divisible by 2
    if diff % 2 != 0:
        return None
    return diff // 2

# def find_sum_swap(arr_a: list[int], arr_b: list[int]) -> Optional[Tuple[int, int]]:
# # def sum_swap_optimal(arr_a: list[int], arr_b: list[int]) -> Optional[Tuple[int, int]]:

#     # Hash set lookup for delta
#     # delta = (S_a - S_b) / 2, only when integer
#     # time: O(A + B), Auxiliary space: O(B)

#     # delta
#     target_diff = _compute_target_difference(arr_a, arr_b)
#     if target_diff is None:
#         return None

#     set_b = set(arr_b)
#     for a in arr_a:
#         target_b = a - target_diff
#         if target_b in set_b: # O(1) lookups due to set
#             return (a, target_b)

#     return None

def find_sum_swap(arr_a: list[int], arr_b: list[int]) -> Optional[Tuple[int, int]]:
# def sum_swap_ctci_sorted(arr_a: list[int], arr_b: list[int]) -> Optional[tuple[int, int]]:

    # time O(A log A + B log B)
    # Space O(1)
    # Sort + 2 pointer approach as in book solutions
    target_diff = _compute_target_difference(arr_a, arr_b)
    if target_diff is None:
        return None

    sorted_a = sorted(arr_a)
    sorted_b = sorted(arr_b)

    i, j = 0, 0

    while i < len(sorted_a) and j < len(sorted_b):
        curr_diff = sorted_a[i] - sorted_b[j]
        if curr_diff == target_diff:
            return (sorted_a[i], sorted_b[j])
        elif curr_diff < target_diff:
            # increase the current difference
            i += 1
        else:
            j += 1

    return None

# =====================================================================
# TEST SUITE
# =====================================================================
class TestSumSwap(unittest.TestCase):

    def test_01_empty_arrays(self):
        """Empty input arrays return None."""
        self.assertIsNone(find_sum_swap([], [1, 2]))
        self.assertIsNone(find_sum_swap([1, 2], []))

    def test_02_odd_sum_difference(self):
        """Difference between sums is odd, so equal sum split is impossible."""
        self.assertIsNone(find_sum_swap([1, 3], [2, 3]))

    def test_03_no_valid_pair_exists(self):
        """Even sum difference, but no matching pair values exist in arrays."""
        # arr1 sum = 3, arr2 sum = 13 -> target_diff = -5
        # Requires b = a + 5. For a=1 -> b=6 (missing); for a=2 -> b=7 (missing).
        self.assertIsNone(find_sum_swap([1, 2], [4, 9]))

    def test_04_already_equal_sums(self):
        """Arrays already have equal sum, returns pair with identical values if available."""
        res = find_sum_swap([1, 2, 3], [2, 2, 2])
        self.assertIsNotNone(res)
        self.assertEqual(res[0], res[1])

    def test_05_ctci_example(self):
        """CTCI example: arr1=[4, 1, 2, 1, 1, 2], arr2=[3, 6, 3, 3] -> valid swap pair."""
        arr1 = [4, 1, 2, 1, 1, 2]
        arr2 = [3, 6, 3, 3]
        res = find_sum_swap(arr1, arr2)
        self.assertIsNotNone(res)
        self.assertEqual(sum(arr1) - res[0] + res[1], sum(arr2) - res[1] + res[0])

    def test_06_negative_numbers(self):
        """Handles negative numbers correctly in target calculation."""
        # arr1 sum = 7, arr2 sum = 11 -> target_diff = -2 -> b = a + 2
        # For a = -1 -> b = 1, which exists in arr2.
        arr1 = [-1, 3, 5]   # sum = 7
        arr2 = [1, 4, 6]    # sum = 11
        res = find_sum_swap(arr1, arr2)
        self.assertIsNotNone(res)
        self.assertEqual(sum(arr1) - res[0] + res[1], sum(arr2) - res[1] + res[0])

# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.21 - Sum Swap\n{'='*75}")

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
    run_tests(TestSumSwap)