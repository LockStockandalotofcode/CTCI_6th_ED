import unittest

def _sign(x: int) -> int:
    # helper returns sign 1 if x is positive 0 if negative without comparison
    sign_bit = (x >> 31) & 1
    return 1 ^ sign_bit

def get_max(a: int, b: int) -> int:
    # Optimal: using bitwise operations and avoiding overflow
    # i.e., we must avoid subtracting a and b, when they are different sign, this might lead to overflow
    # time O(1), space O(1)

    d = a - b # d for difference
    sa = _sign(a)
    sb = _sign(b)
    sd = _sign(d)

    # check if a and b have different signs
    use_sign_a = sa ^ sb # 1 if signs are different, 0 if same
    use_sign_d = 1 ^ use_sign_a # to use diff or not, 0 if signs are different, 1 if same

    # if different signs, k = sa
    # if same signs, k = sd
    k = (use_sign_a * sa) + (use_sign_d * sd)
    q = 1 ^ k # opposite of k

    return (a * k) + (b * q)

# =====================================================================
# TEST SUITE
# =====================================================================
class TestNumberMax(unittest.TestCase):

    def test_01_both_positive_a_greater(self):
        """Both positive numbers where a > b."""
        self.assertEqual(get_max(10, 5), 10)

    def test_02_both_positive_b_greater(self):
        """Both positive numbers where b > a."""
        self.assertEqual(get_max(3, 18), 18)

    def test_03_equal_numbers(self):
        """Equal numbers return the value itself."""
        self.assertEqual(get_max(7, 7), 7)

    def test_04_opposite_signs_positive_max(self):
        """Positive number vs negative number."""
        self.assertEqual(get_max(15, -20), 15)
        self.assertEqual(get_max(-100, 1), 1)

    def test_05_both_negative(self):
        """Both negative numbers."""
        self.assertEqual(get_max(-5, -15), -5)
        self.assertEqual(get_max(-50, -10), -10)

    def test_06_zero_comparison(self):
        """Comparisons involving zero."""
        self.assertEqual(get_max(0, 5), 5)
        self.assertEqual(get_max(-5, 0), 0)


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.7 - Number Max\n{'='*75}")

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
    run_tests(TestNumberMax)