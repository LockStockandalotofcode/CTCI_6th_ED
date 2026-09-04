import bisect
import unittest

Person = tuple[int, int]

def _lis_sorting(weights: list[int]) -> int:
    tails: list[int] = []
    for w in weights:
        idx = bisect.bisect_left(tails, w)
        if idx == len(tails):
            tails.append(w)
        else:
            tails[idx] = w
    return len(tails)

def best_tower(people: list[Person]) -> int:
    if not people:
        return 0

    # Sort key: height ascending, 
    # weight descending for equal height so we dont pick same height in step 2
    sorted_people = sorted(people, key=lambda p: (p[0], -p[1]))

    # extract weight and run LIS
    weights = [p[1] for p in sorted_people]
    return _lis_sorting(weights)


# # =====================================================================
# # SOLUTION PLACEHOLDER
# # Replace or import your actual function here
# # =====================================================================
# def best_tower(people: list[tuple[int, int]]) -> int:
#     """Calculates max tower height where height and weight are strictly increasing.
#     Each person is represented as a tuple: (height, weight).
#     """
#     if not people:
#         return 0

#     # Sort height ascending; for same height, sort weight descending
#     sorted_people = sorted(people, key=lambda x: (x[0], -x[1]))

#     # Longest Increasing Subsequence (LIS) on weight
#     tails = []
#     for _, weight in sorted_people:
#         idx = bisect.bisect_left(tails, weight)
#         if idx == len(tails):
#             tails.append(weight)
#         else:
#             tails[idx] = weight

#     return len(tails)


# =====================================================================
# TEST SUITE
# =====================================================================
class TestCircusTower(unittest.TestCase):

    def test_01_empty_input(self):
        """Empty input list returns 0 tower height."""
        self.assertEqual(best_tower([]), 0)

    def test_02_single_person(self):
        """Single person returns tower height of 1."""
        self.assertEqual(best_tower([(65, 100)]), 1)

    def test_03_already_sorted_increasing(self):
        """Strictly increasing height and weight returns full length."""
        people = [(60, 100), (65, 110), (70, 120)]
        self.assertEqual(best_tower(people), 3)

    def test_04_same_heights_conflict(self):
        """Cannot stack people with identical heights."""
        people = [(65, 100), (65, 150), (65, 200)]
        self.assertEqual(best_tower(people), 1)

    def test_05_unordered_inputs(self):
        """Unordered people set finds max valid LIS sequence."""
        people = [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]
        self.assertEqual(best_tower(people), 6)

    def test_06_same_weights_conflict(self):
        """Cannot stack people with identical weights."""
        people = [(60, 100), (65, 100), (70, 100)]
        self.assertEqual(best_tower(people), 1)


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.8 - Circus Tower\n{'='*75}")

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
    run_tests(TestCircusTower)