import unittest

def smallest_difference(array_a: list[int], array_b: list[int]) -> int:
    if not array_a or not array_b:
        raise ValueError("Both Input must be non-emoty")
    # starting with sorted array
    s_a = sorted(array_a)
    # sorted
    s_b = sorted(array_b)
    # 2 - pointer approach
    a, b = 0, 0
    # keep a running min, to track the minimum element
    min_diff = float("inf")
    # increment the lower element 
    while a < len(s_a) and b < len(s_b):
        min_diff = min(min_diff, abs(s_a[a] - s_b[b]))
        if s_a[a] <= s_b[b]:
            a += 1
        else:
            b += 1
    # the lower element reaches the end first, so if one array is exhausted, we have our result
    # incrementing the other is anyways only going to increase the difference
    return min_diff

# # =====================================================================
# # SOLUTION PLACEHOLDER
# # Replace or import your actual function here
# # =====================================================================
# def smallest_difference(array_a: list[int], array_b: list[int]) -> int:
#     """Finds the smallest non-negative difference between any pair of values across two arrays."""
#     if not array_a or not array_b:
#         raise ValueError("Both input arrays must be non-empty.")

#     array_a.sort()
#     array_b.sort()

#     i, j = 0, 0
#     min_diff = float("inf")

#     while i < len(array_a) and j < len(array_b):
#         diff = abs(array_a[i] - array_b[j])
#         min_diff = min(min_diff, diff)

#         if array_a[i] < array_b[j]:
#             i += 1
#         else:
#             j += 1

#     return int(min_diff)


# =====================================================================
# TEST SUITE
# =====================================================================
class TestSmallestDifference(unittest.TestCase):

    def test_01_empty_arrays_raise_value_error(self):
        """Passing an empty array raises a ValueError."""
        with self.assertRaises(ValueError):
            smallest_difference([], [1, 2, 3])
        with self.assertRaises(ValueError):
            smallest_difference([1, 2, 3], [])

    def test_02_single_element_in_each(self):
        """Single element in each array returns absolute difference."""
        self.assertEqual(smallest_difference([5], [12]), 7)

    def test_03_exact_match_zero_difference(self):
        """Exact value match across arrays returns 0 difference."""
        self.assertEqual(smallest_difference([1, 5, 10], [20, 5, 30]), 0)

    def test_04_ctci_example(self):
        """CTCI example: A = [1,3,15,11,2], B = [23,127,235,19,8] -> Min diff is 3 (11 and 8)."""
        a = [1, 3, 15, 11, 2]
        b = [23, 127, 235, 19, 8]
        self.assertEqual(smallest_difference(a, b), 3)

    def test_05_all_negative_numbers(self):
        """Negative numbers handled correctly."""
        a = [-10, -5, -1]
        b = [-8, -3]
        self.assertEqual(smallest_difference(a, b), 2)

    def test_06_disjoint_ranges(self):
        """Arrays with non-overlapping ranges."""
        a = [1, 2, 3]
        b = [100, 200, 300]
        self.assertEqual(smallest_difference(a, b), 97)

    def test_07_duplicates_in_arrays(self):
        """Duplicate values handled properly."""
        self.assertEqual(smallest_difference([4, 4, 4], [8, 4, 12]), 0)

    def test_08_interleaved_elements(self):
        """Interleaved value ranges."""
        a = [10, 30, 50]
        b = [20, 40, 60]
        self.assertEqual(smallest_difference(a, b), 10)


# =====================================================================
# INFORMATIVE TEST RUNNER
# =====================================================================
def run_informative_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.6 - Smallest Difference\n{'='*75}")

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
    run_informative_tests(TestSmallestDifference)