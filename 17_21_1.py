import unittest

def volume_of_histogram(histo: list[int]) -> int:
    # 2 sweeps through the array of heights 
    # one to track the left maxes: tallest bar on the left
    # another to track the right maxes: tallest bar on the right, 
    # in 2nd sweep merge the other steps: track the minimum of the 2 maxes, this governs the height
    # then next, we get total volume by summing volume above each bar(volume at this bar - thhis bar's own height)
    if not histo:
        return 0
    s = len(histo)
    result = [0] * s
    left_max = 0
    for i in range(s):
        left_max = max(left_max, histo[i])
        result[i] = left_max

    right_max = 0
    for i in range(s-1, -1, -1):
        right_max = max(right_max, histo[i])
        vol = min(result[i], right_max)
        result[i] = vol - histo[i]

    return sum(result)

# =====================================================================
# SOLUTION PLACEHOLDER
# Replace or import your actual function here
# =====================================================================
# def volume_of_histogram(histo: list[int]) -> int:
#     """Calculates trapped water in a histogram using two pointers."""
#     if not histo or len(histo) < 3:
#         return 0

#     left, right = 0, len(histo) - 1
#     result, right_max = histo[left], histo[right]
#     water = 0

#     while left < right:
#         if histo[left] < histo[right]:
#             if histo[left] >= result:
#                 result = histo[left]
#             else:
#                 water += result - histo[left]
#             left += 1
#         else:
#             if histo[right] >= right_max:
#                 right_max = histo[right]
#             else:
#                 water += right_max - histo[right]
#             right -= 1

#     return water


# =====================================================================
# TEST SUITE
# =====================================================================
class TestVolumeOfHistogram(unittest.TestCase):

    def test_01_empty_histogram(self):
        """Empty list returns 0 trapped water."""
        self.assertEqual(volume_of_histogram([]), 0)

    def test_02_insufficient_bars(self):
        """Fewer than 3 bars cannot trap water."""
        self.assertEqual(volume_of_histogram([5]), 0)
        self.assertEqual(volume_of_histogram([5, 10]), 0)

    def test_03_flat_histogram(self):
        """Flat histogram (equal bar heights) traps no water."""
        self.assertEqual(volume_of_histogram([3, 3, 3, 3, 3]), 0)

    def test_04_strictly_increasing(self):
        """Strictly ascending height bars trap no water."""
        self.assertEqual(volume_of_histogram([1, 2, 3, 4, 5]), 0)

    def test_05_strictly_decreasing(self):
        """Strictly descending height bars trap no water."""
        self.assertEqual(volume_of_histogram([5, 4, 3, 2, 1]), 0)

    def test_06_simple_v_shape(self):
        """Simple V-shaped valley [5, 0, 5] traps 5 units."""
        self.assertEqual(volume_of_histogram([5, 0, 5]), 5)

    def test_07_trapped_between_step(self):
        """Asymmetric valley [4, 2, 3] traps 1 unit."""
        self.assertEqual(volume_of_histogram([4, 2, 3]), 1)

    def test_08_ctci_example(self):
        """CTCI 17.21 example histogram returns 26 units."""
        histo = [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]
        self.assertEqual(volume_of_histogram(histo), 26)

    def test_09_classic_trapping_rain_water(self):
        """Standard LeetCode histogram traps 6 units."""
        self.assertEqual(volume_of_histogram([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6)

    def test_10_plateau_valleys(self):
        """Multiple flat low bars trapped between high walls."""
        self.assertEqual(volume_of_histogram([4, 1, 1, 1, 4]), 9)

    def test_11_unequal_bounding_peaks(self):
        """Peaks of different heights bounding multiple valleys."""
        self.assertEqual(volume_of_histogram([4, 2, 0, 3, 2, 5]), 9)


# =====================================================================
# INFORMATIVE TEST RUNNER
# =====================================================================
def run_informative_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.21 - Volume of Histogram\n{'='*75}")

    passed, failed, errors = 0, 0, 0
    failures_details = []

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
            for _, err in result.failures:
                failures_details.append((test_name, doc, err))
        elif result.errors:
            print(f"  ⚠️  [ERROR] {desc}")
            errors += 1
            for _, err in result.errors:
                failures_details.append((test_name, doc, err))

    total = passed + failed + errors
    pass_rate = (passed / total * 100) if total > 0 else 0.0

    print(f"\n{'-'*75}")
    print(f" EXECUTION SUMMARY:")
    print(f" Total Tests : {total}")
    print(f" Passed      : {passed} ✅")
    print(f" Failed      : {failed} ❌")
    print(f" Errors      : {errors} ⚠️")
    print(f" Success Rate: {pass_rate:.1f}%")
    print(f"{'='*75}\n")

    # if failures_details:
    #     print(f"{'!'*75}\n DETAILED FAILURE / ERROR REPORT:\n{'!'*75}")
    #     for name, doc, err in failures_details:
    #         print(f"• Test: {name}\n  Description: {doc}\n  Traceback:\n{err}\n{'-'*75}")


if __name__ == "__main__":
    run_informative_tests(TestVolumeOfHistogram)