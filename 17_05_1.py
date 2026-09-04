import unittest
from typing import Union, Optional

Element = Union[str, int]

def _is_letter(item: Element) -> bool:
    # checks if letter or not 
    return isinstance(item, str) and item.isalpha()

# LIS longest increaing subsequence: 
def find_longest_subarray(arr: list[Element]) -> list[Element]:
    if not arr:
        return []

    # Map prefix sum -> first index seen
    # Base case: prefix sum 0 occurs at index -1
    first_seen = {0 : -1}

    running_sum = 0
    max_len = 0
    best_bounds: Optional[tuple[int, int]] = None
    for i, item in enumerate(arr):
        # add 1, for letter, -1 for digit
        # sum == 0 means equal freq of digits and letters
        running_sum += 1 if _is_letter(item) else -1

        if running_sum in first_seen:
            start_idx = first_seen[running_sum] + 1
            length = i - first_seen[running_sum]
            if length > max_len:
                max_len = length
                best_bounds = (start_idx, i)
        else:
            first_seen[running_sum] = i

    if best_bounds is None:
        return []

    start, end = best_bounds
    return arr[start: end + 1]


# =====================================================================
# TEST SUITE
# =====================================================================
class TestLettersAndNumbers(unittest.TestCase):

    def test_01_empty_array(self):
        """Empty input array returns empty list."""
        self.assertEqual(find_longest_subarray([]), [])

    def test_02_all_letters(self):
        """Array containing only letters returns empty list."""
        self.assertEqual(find_longest_subarray(["a", "b", "c"]), [])

    def test_03_all_numbers(self):
        """Array containing only digits returns empty list."""
        self.assertEqual(find_longest_subarray(["1", "2", "3"]), [])

    def test_04_entire_array_balanced(self):
        """Entire array is balanced, returning the full array."""
        arr = ["a", "1", "b", "2"]
        self.assertEqual(find_longest_subarray(arr), ["a", "1", "b", "2"])

    def test_05_ctci_example(self):
        """CTCI example array finding longest balanced sub-segment."""
        arr = [
            'A',
            '1',
            'B',
            'C',
            'D',
            '2',
            '3',
            '4',
            'E',
            '5',
            '6',
            '7',
            'F',
            'G',
        ]
        res = find_longest_subarray(arr)
        # Result should have equal letters and digits and length 12
        letters = sum(1 for x in res if str(x).isalpha())
        digits = sum(1 for x in res if str(x).isdigit())
        self.assertEqual(letters, digits)
        self.assertEqual(len(res), 14)

    def test_06_earliest_subarray_preference(self):
        """When multiple balanced subarrays have equal length, returns the earliest."""
        arr = ["a", "1", "b", "2"]
        self.assertEqual(find_longest_subarray(arr), ["a", "1", "b", "2"])


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(
        f"\n{'='*75}\n TEST SUITE: CTCI 17.5 - Letters and Numbers\n{'='*75}"
    )

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
    print(
        f" SUMMARY: Total: {total} | Passed: {passed} ✅ | Failed: {failed} ❌ | Errors: {errors} ⚠️ | Rate: {pass_rate:.1f}%"
    )
    print(f"{'='*75}\n")


if __name__ == "__main__":
    run_tests(TestLettersAndNumbers)