import random
import unittest

def rand5() -> int:
    # helper: for rand5, range [1, 5]
    return random.randint(1, 5)

def _generate_base5_range25() -> int:
    # generates uniform range [0, 24] using base-5 conversion
    return 5 * (rand5() - 1) + (rand5() - 1)

def rand7() -> int:
    # Rejection sampling via Base-5 expansion
    # time: O(1) 
    # Space: O(1)

    while True:
        num = _generate_base5_range25()
        if num < 21:
            return (num % 7) + 1


# =====================================================================
# TEST SUITE
# =====================================================================
class TestRand7FromRand5(unittest.TestCase):

    def test_01_output_range_validity(self):
        """All generated values remain within range [1, 7]."""
        for _ in range(1000):
            val = rand7()
            self.assertTrue(1 <= val <= 7)

    def test_02_distribution_uniformity(self):
        """Generated distribution across 70,000 runs is roughly equal (~10,000 per bucket)."""
        counts = {i: 0 for i in range(1, 8)}
        trials = 70000

        for _ in range(trials):
            counts[rand7()] += 1

        expected_per_bucket = trials // 7
        for num, count in counts.items():
            # Allow +- 10% tolerance for randomness
            self.assertTrue(
                expected_per_bucket * 0.9 <= count <= expected_per_bucket * 1.1,
                f"Bucket {num} count {count} out of expected range.",
            )

    def test_03_returns_integer_type(self):
        """Return value is an instance of int."""
        self.assertIsInstance(rand7(), int)


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(
        f"\n{'='*75}\n TEST SUITE: CTCI 16.23 - Rand7 from Rand5\n{'='*75}"
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
            fail_msg = result.failures[0][1].strip().split("\n")[-1]
            print(f"  ❌ [FAIL] {desc} | {fail_msg}")
            failed += 1
        elif result.errors:
            err_msg = result.errors[0][1].strip().split("\n")[-1]
            print(f"  ⚠️  [ERROR] {desc} | {err_msg}")
            errors += 1

    total = passed + failed + errors
    pass_rate = (passed / total * 100) if total > 0 else 0.0

    print(f"\n{'-'*75}")
    print(
        f" SUMMARY: Total: {total} | Passed: {passed} ✅ | Failed: {failed} ❌ | Errors: {errors} ⚠️ | Rate: {pass_rate:.1f}%"
    )
    print(f"{'='*75}\n")


if __name__ == "__main__":
    run_tests(TestRand7FromRand5)