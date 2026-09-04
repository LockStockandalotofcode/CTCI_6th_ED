import unittest

def add_without_plus(a: int, b: int) -> int:
    # use bitmask to keep number within bounds at all times
    # XOR = sum without carry
    # & << 1 = sum with carry
    MASK = 0xFFFFFFFF
    MAX_INT = 0x7FFFFFFF

    while b != 0: # no more carry remains
        sum_wo_carry = (a ^ b) & MASK
        carry = ((a & b) << 1) & MASK

        a = sum_wo_carry
        b = carry

    return a if a <= MAX_INT else ~(a ^ MASK)


# =====================================================================
# TEST SUITE
# =====================================================================
class TestAddWithoutPlus(unittest.TestCase):

    def test_01_both_zero(self):
        """0 + 0 = 0."""
        self.assertEqual(add_without_plus(0, 0), 0)

    def test_02_positive_integers(self):
        """Addition of two positive integers."""
        self.assertEqual(add_without_plus(75, 25), 100)

    def test_03_positive_and_negative(self):
        """Addition of positive and negative integers."""
        self.assertEqual(add_without_plus(15, -5), 10)
        self.assertEqual(add_without_plus(-15, 5), -10)

    def test_04_both_negative(self):
        """Addition of two negative integers."""
        self.assertEqual(add_without_plus(-20, -30), -50)

    def test_05_identity_with_zero(self):
        """Adding zero to positive and negative numbers."""
        self.assertEqual(add_without_plus(0, -42), -42)
        self.assertEqual(add_without_plus(100, 0), 100)

    def test_06_carrying_bits(self):
        """Triggers carry propagation through multiple bit positions."""
        self.assertEqual(add_without_plus(1, 15), 16)


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.1 - Add Without Plus\n{'='*75}")

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
    run_tests(TestAddWithoutPlus)