import unittest
from typing import Optional, List


def _find_candidate(nums: list[int]) -> Optional[int]:
    # helper: finds potential candidate, not necessarily majority 
    # more like last one standing
    candidate = nums[0]
    count = 1
    for num in nums:
        if count == 0:
            candidate = num
            count += 1
        elif num != candidate:
            count -= 1
        elif num == candidate:
            count += 1
    return candidate

def _validate_candidate(nums: list[int], candidate: int) -> bool:
    # helper: validates potential candidate for being truly majority
    if candidate is None:
        return False

    frequency = sum(1 for x in nums if x == candidate)
    return frequency > len(nums) // 2

def majority_element(nums: list[int]) -> int:

    # Boyer Moore Majority Voting Algorithm
    # without needing hashtable, thus reducing space to O(1)
    # time: O(N), space: O(1)

    if not nums:
        return -1

    candidate = _find_candidate(nums)
    return candidate if _validate_candidate(nums, candidate) else -1

# =====================================================================
# TEST SUITE
# =====================================================================
class TestMajorityElement(unittest.TestCase):

    def test_01_empty_list(self):
        """Empty list returns -1."""
        self.assertEqual(majority_element([]), -1)

    def test_02_single_element(self):
        """Single element list returns that element."""
        self.assertEqual(majority_element([42]), 42)

    def test_03_clear_majority(self):
        """Clear majority element present in > 50% of positions."""
        self.assertEqual(majority_element([1, 2, 5, 9, 5, 9, 5, 5, 5]), 5)

    def test_04_no_majority_even_split(self):
        """No majority element exists (equal distribution)."""
        self.assertEqual(majority_element([1, 2, 1, 2]), -1)

    def test_05_exactly_half_not_majority(self):
        """Element appearing exactly N/2 times is not a majority (> N/2 required)."""
        self.assertEqual(majority_element([3, 3, 4, 4]), -1)

    def test_06_all_identical_elements(self):
        """All elements in list are identical."""
        self.assertEqual(majority_element([7, 7, 7, 7, 7]), 7)

    def test_07_negative_numbers_majority(self):
        """Majority element logic with negative integers."""
        self.assertEqual(majority_element([-1, -1, -1, 2, 3]), -1)


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.10 - Majority Element\n{'='*75}")

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
    run_tests(TestMajorityElement)