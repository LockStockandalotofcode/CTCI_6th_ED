import unittest

def _count_twos_at_digit_place(n: int, power_of_ten: int) -> int:
    next_power = power_of_ten * 10

    digit = (n // power_of_ten) % 10
    # complete 10 * power_of_ten cycles
    total = (n // (next_power)) * power_of_ten

    # partial cycle evaluation
    if digit == 2:
        total += (n % power_of_ten) + 1
    elif digit > 2:
        total += (power_of_ten)
    
    # each power_of_ten (P) has P many 2's at P place
    # eg. 100 = 10 * 10, has 10 2's at TENs place
    return total

def count_twos(n: int) -> int:
    # Digit by digit Combinatorics
    # TIME: O(log_10 N)
    # Auxiliary space: O(1)

    if n < 2:
        return 0

    total_twos = 0
    power_of_ten = 1

    while power_of_ten <= n:
        total_twos += _count_twos_at_digit_place(n, power_of_ten)
        power_of_ten *= 10

    return total_twos

# =====================================================================
# TEST SUITE
# =====================================================================
class TestCountOfTwos(unittest.TestCase):

    def test_01_zero_and_negative_inputs(self):
        """0 or negative input returns 0."""
        self.assertEqual(count_twos(0), 0)
        self.assertEqual(count_twos(-15), 0)

    def test_02_single_digits(self):
        """Single digit inputs."""
        self.assertEqual(count_twos(1), 0)
        self.assertEqual(count_twos(2), 1)
        self.assertEqual(count_twos(9), 1)

    def test_03_up_to_twenty(self):
        """Up to 20 returns 3 (2, 12, 20)."""
        self.assertEqual(count_twos(20), 3)

    def test_04_up_to_twenty_five(self):
        """Up to 25 includes 22 with two 2s (Total: 9)."""
        self.assertEqual(count_twos(25), 9)

    def test_05_hundred_boundary(self):
        """Up to 100 returns 20."""
        self.assertEqual(count_twos(100), 20)

    def test_06_large_number(self):
        """Large input N = 61523."""
        self.assertEqual(count_twos(61523), 34507)

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
    run_tests(TestCountOfTwos, "CTCI 17.6 - Count of 2s")