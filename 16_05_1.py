import unittest

def _count_factors_of_five(n: int) -> int:
    # helper method iteratively counts factors of 5 in n!
    count = 0
    divisor = 5

    while n >= divisor:
        count = count + (n // divisor)
        # // gives the desired floor as per mathematical formula
        divisor = divisor * 5

    return count

def count_factorial_zeroes(n: int) -> int:
    # facotrs of 5 governs no. of trailing zeroes
    # both 5 and 2 do, but since 2 is always more frequent in factorial, freq of 5 decides 

    # Time O(log_5 N), auxiliary space: O(1)
    if n < 0:
        # raise ValueError("Factorials are undefined for negative numbers")
        return -1

    return _count_factors_of_five(n)

# =====================================================================
# TEST SUITE
# =====================================================================
class TestFactorialZeros(unittest.TestCase):

    def test_01_negative_input(self):
        """Negative numbers return -1 (invalid factorial input)."""
        self.assertEqual(count_factorial_zeroes(-5), -1)

    def test_02_zero_and_small_inputs(self):
        """n = 0 through 4 have 0 trailing zeros (0! = 1, 4! = 24)."""
        self.assertEqual(count_factorial_zeroes(0), 0)
        self.assertEqual(count_factorial_zeroes(4), 0)

    def test_03_first_trailing_zero(self):
        """5! = 120, yielding 1 trailing zero."""
        self.assertEqual(count_factorial_zeroes(5), 1)

    def test_04_multiple_five_factors(self):
        """25! yields 6 trailing zeros due to 5^2 factor contribution."""
        self.assertEqual(count_factorial_zeroes(25), 6)

    def test_05_large_input_100(self):
        """100! yields 24 trailing zeros."""
        self.assertEqual(count_factorial_zeroes(100), 24)

    def test_06_boundary_just_before_and_after_25(self):
        """24! yields 4 zeros while 25! yields 6 zeros."""
        self.assertEqual(count_factorial_zeroes(24), 4)
        self.assertEqual(count_factorial_zeroes(25), 6)


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.5 - Factorial Zeros\n{'='*75}")

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
    run_tests(TestFactorialZeros)