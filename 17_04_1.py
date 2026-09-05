import unittest

def _get_bit(number: int, bit_idx: int) -> int:
    return (number >> bit_idx) & 1

def _find_missing_recursive(numbers: list[int], column: int) -> int:
    if column >= 32:
        return 0

    zeros = []
    ones = []

    for num in numbers:
        if _get_bit(num, column) == 0:
            zeros.append(num)
        else:
            ones.append(num)

    # if count of 0s <= count of 1s, missing number has 0
    #  else it has 1; even in base case, it is 1
    if len(zeros) <= len(ones):
        v = _find_missing_recursive(zeros, column + 1)
        return (v << 1) | 0
    else:
        v = _find_missing_recursive(ones, column + 1)
        return (v << 1) | 1
            

def find_missing_number_r(arr: list[int]) -> int:
    # recursive solution
    # Bit Column partitioning
    # extracting 1 or 0 in the digits place, then making the number
    # Time : O(N)
    # Space: O(N)
    return _find_missing_recursive(arr, 0)

# Iterative
# avoids call stack overhead
# Time: O(N), Space: O(N)
def find_missing_number(arr: list[int]) -> int:
    remaining = list(arr)
    missing_number = 0
    column = 0

    while column < 32 and remaining:
        zeros = []
        ones = []

        for num in remaining:
            if _get_bit(num, column) == 0:
                zeros.append(num)
            else:
                ones.append(num)

        if len(zeros) <= len(ones):
            remaining = zeros
            # Missing number bit at current column is 0
            # no need to set bit
        else:
            remaining = ones
            missing_number = missing_number | (1 << column)

        column += 1

    return missing_number

# # =====================================================================
# # SOLUTION PLACEHOLDER
# # =====================================================================
# def find_missing_number(nums: list[int]) -> int:
#     """Finds the single missing number from an array containing 0 to N."""
#     n = len(nums)
#     expected_sum = n * (n + 1) // 2
#     return expected_sum - sum(nums)

# =====================================================================
# TEST SUITE
# =====================================================================
class TestMissingNumber(unittest.TestCase):

    def test_01_missing_zero(self):
        """Missing element is 0."""
        self.assertEqual(find_missing_number([1, 2, 3]), 0)

    def test_02_missing_last(self):
        """Missing element is N (largest)."""
        self.assertEqual(find_missing_number([0, 1, 2, 3]), 4)

    def test_03_missing_middle(self):
        """Missing element is in the middle."""
        self.assertEqual(find_missing_number([0, 1, 3, 4]), 2)

    def test_04_single_element_missing_zero(self):
        """Single element array missing 0."""
        self.assertEqual(find_missing_number([1]), 0)

    def test_05_single_element_missing_one(self):
        """Single element array missing 1."""
        self.assertEqual(find_missing_number([0]), 1)

    def test_06_unsorted_input(self):
        """Unsorted input array."""
        self.assertEqual(find_missing_number([3, 0, 1]), 2)

    def test_07_large_array(self):
        """Large array missing arbitrary element."""
        full = list(range(1001))
        full.remove(420)
        self.assertEqual(find_missing_number(full), 420)


# =====================================================================
# CONCISE SINGLE-LINE TEST RUNNER
# =====================================================================
def run_tests(test_class, title: str):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: {title}\n{'='*75}")

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
            err_msg = result.failures[0][1].strip().splitlines()[-1]
            print(f"  ❌ [FAIL] {desc} | Details: {err_msg}")
            failed += 1
        elif result.errors:
            err_msg = result.errors[0][1].strip().splitlines()[-1]
            print(f"  ⚠️  [ERROR] {desc} | Details: {err_msg}")
            errors += 1

    total = passed + failed + errors
    pass_rate = (passed / total * 100) if total > 0 else 0.0

    print(f"{'-'*75}")
    print(f" SUMMARY: Total: {total} | Passed: {passed} ✅ | Failed: {failed} ❌ | Errors: {errors} ⚠️ | Rate: {pass_rate:.1f}%")
    print(f"{'='*75}\n")


if __name__ == "__main__":
    run_tests(TestMissingNumber, "CTCI 17.4 - Missing Number")