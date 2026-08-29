import unittest
def pair_sums(arr: list[int], target: int) -> list[tuple[int, int]]:
    if not arr:
        return []
    
    s = len(arr)
    result = []
    visited_indices = []
    for i in range(s):
        curr_target = target - arr[i]
        if i not in visited_indices:
            for j in range(i + 1, s):
                if arr[j] == curr_target:
                    visited_indices.append(i)
                    visited_indices.append(j)
                    result.append((arr[i], arr[j]))
                    break

    return result

# =====================================================================
# TEST SUITE
# =====================================================================
class TestPairsWithSum(unittest.TestCase):

    def normalize_pairs(self, pairs: list[tuple[int, int]]) -> list[tuple[int, int]]:
        """Standardizes pair order for order-independent assertions."""
        return sorted([tuple(sorted(p)) for p in pairs])

    def test_01_empty_array(self):
        """Empty array returns empty list."""
        self.assertEqual(pair_sums([], 10), [])

    def test_02_single_element(self):
        """Single element cannot form a pair."""
        self.assertEqual(pair_sums([5], 5), [])

    def test_03_no_matching_pairs(self):
        """Array with no valid pairs returns empty list."""
        self.assertEqual(pair_sums([1, 2, 3, 4], 100), [])

    def test_04_single_matching_pair(self):
        """Single valid pair in array."""
        result = pair_sums([1, 4], 5)
        self.assertEqual(self.normalize_pairs(result), [(1, 4)])

    def test_05_multiple_distinct_pairs(self):
        """Multiple distinct valid pairs."""
        result = pair_sums([-2, -1, 0, 3, 5, 6, 7, 9], 7)
        expected = [(-2, 9), (0, 7)]
        self.assertEqual(self.normalize_pairs(result), self.normalize_pairs(expected))

    def test_06_duplicate_elements_even_count(self):
        """Even duplicates consumed correctly: [2, 2, 2, 2] with target 4 -> 2 pairs."""
        result = pair_sums([2, 2, 2, 2], 4)
        self.assertEqual(self.normalize_pairs(result), [(2, 2), (2, 2)])

    def test_07_duplicate_elements_odd_count(self):
        """Odd duplicates leave 1 element unconsumed: [2, 2, 2] with target 4 -> 1 pair."""
        result = pair_sums([2, 2, 2], 4)
        self.assertEqual(self.normalize_pairs(result), [(2, 2)])

    def test_08_negative_numbers_and_zero_target(self):
        """Negative numbers summing to 0 target."""
        result = pair_sums([-3, 3, -5, 5, 0, 0], 0)
        expected = [(-5, 5), (-3, 3), (0, 0)]
        self.assertEqual(self.normalize_pairs(result), self.normalize_pairs(expected))

    def test_09_large_array_accuracy(self):
        """Large range array validation (-500 to 500)."""
        arr = list(range(-500, 501))
        result = pair_sums(arr, 0)
        self.assertEqual(len(result), 500)


# =====================================================================
# INFORMATIVE TEST RUNNER
# =====================================================================
def run_informative_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.24 - Pairs with Sum\n{'='*75}")

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


if __name__ == "__main__":
    run_informative_tests(TestPairsWithSum)