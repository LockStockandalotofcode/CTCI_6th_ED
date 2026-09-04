import unittest

def swap_numbers(a: int, b: int) -> tuple[int, int]:
    a = a ^ b # stores combined bit mask of both numbers in a 
    b = a ^ b  # b now holds original a
    a = a ^ b # a now holds original b

    return (a, b)

# def swap_numbers(a: int, b: int) -> tuple[int, int]:
#     # using arithmetic subtraction, cannot handle integer overflow
#     a = a - b # stores difference of both numbers in a 
#     b = a + b  # b now holds original a
#     a = b - a # a now holds original b

#     return (a, b)


# =====================================================================
# TEST SUITE
# =====================================================================
class TestNumberSwapper(unittest.TestCase):

    def test_01_positive_numbers(self):
        """Swaps two distinct positive integers."""
        self.assertEqual(swap_numbers(5, 10), (10, 5))
        # self.assertEqual(swap_numbers(5, 10), (10, 5))

    def test_02_identical_numbers(self):
        """Swaps two identical numbers."""
        self.assertEqual(swap_numbers(7, 7), (7, 7))
        # self.assertEqual(swap_numbers(7, 7), (7, 7))

    def test_03_zeros(self):
        """Swaps zeros correctly."""
        self.assertEqual(swap_numbers(0, 0), (0, 0))

    def test_04_negative_and_positive(self):
        """Swaps a negative integer with a positive integer."""
        self.assertEqual(swap_numbers(-5, 12), (12, -5))

    def test_05_both_negative(self):
        """Swaps two negative integers."""
        self.assertEqual(swap_numbers(-30, -50), (-50, -30))

    def test_06_large_integers(self):
        """Swaps large integers without overflow."""
        self.assertEqual(
            swap_numbers(1000000000, 2000000000), (2000000000, 1000000000)
        )


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.1 - Number Swapper\n{'='*75}")

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
    run_tests(TestNumberSwapper)