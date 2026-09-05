import random
import unittest

def _get_random_index(lower_bound: int, upper_bound: int) -> int:
    return random.randint(lower_bound, upper_bound)

def get_random_set(arr: list[int], m: int) -> list[int]:
    # Partial REservoir Sampling, shuffle based off Fisher YAtes 
    # Time: O(N)
    # auxiliary space: O(M)

    n = len(arr)
    if m < 0:
        return []
    if m > len(arr):
        return arr

    result = arr[ : m]
    for i in range(m, n):
        # pick random integer from (0, i)
        # if its < m, swap it with the element
        k = _get_random_index(0, i)
        if k < m:
            result[k] = arr[i]

    return result

# # =====================================================================
# # SOLUTION PLACEHOLDER
# # Replace or import your actual function here
# # =====================================================================
# def get_random_set(arr: list[int], m: int) -> list[int]:
#     """Selects a random sample of m elements from arr using Reservoir Sampling concept."""
#     if m <= 0 or not arr:
#         return []
#     if m >= len(arr):
#         return list(arr)

#     subset = list(arr[:m])
#     for i in range(m, len(arr)):
#         j = random.randint(0, i)
#         if j < m:
#             subset[j] = arr[i]
#     return subset


# =====================================================================
# TEST SUITE
# =====================================================================
class TestRandomSet(unittest.TestCase):

    def test_01_zero_or_negative_m(self):
        """Requesting m <= 0 elements returns empty list."""
        self.assertEqual(get_random_set([1, 2, 3], 0), [])
        self.assertEqual(get_random_set([1, 2, 3], -2), [])

    def test_02_m_greater_than_array_length(self):
        """Requesting m >= array length returns all elements."""
        arr = [10, 20, 30]
        result = get_random_set(arr, 5)
        self.assertEqual(sorted(result), sorted(arr))

    def test_03_exact_sample_size(self):
        """Output subset size matches target m."""
        arr = list(range(100))
        result = get_random_set(arr, 10)
        self.assertEqual(len(result), 10)

    def test_04_subset_validity(self):
        """All elements in result set originate from input array."""
        arr = [10, 20, 30, 40, 50, 60]
        result = get_random_set(arr, 3)
        for item in result:
            self.assertIn(item, arr)

    def test_05_uniqueness_preservation(self):
        """Selected items preserve original array uniqueness constraints."""
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        result = get_random_set(arr, 5)
        self.assertEqual(len(result), len(set(result)))


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.3 - Random Set\n{'='*75}")

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
    run_tests(TestRandomSet)