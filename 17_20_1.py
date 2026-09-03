import heapq
import unittest

# insert(), add_number time = O(log N)
# get_median() time = O(1)
# space = O(N)

# Optimal & same as book solution
# keeps elements sorted at all times

# dual heap
# max-heap for smaller elements
# min-heap for larger elements

# other elements
# keep the two heaps balanced, rebalance if needed
# at any point median is avg of two heap tops for equal size heaps,
# otherwise top of the larger heap

class ContinuousMedian:
    def __init__(self):
        # python by default has min-heaps
        # to simulate max-heap, negate the values while inserting and negate again after popping to get the original value
        self.lower_half_max_heap = []
        self.upper_half_min_heap = []

    def _rebalance_heaps(self) -> None:
        # helper to store size invariant: size difference (of heaps) <= 1
        if len(self.lower_half_max_heap) > len(self.upper_half_min_heap) + 1:
            val = -heapq.heappop(self.lower_half_max_heap)
            heapq.heappush(self.upper_half_min_heap, val)
        elif len(self.lower_half_max_heap) < len(self.upper_half_min_heap):
            val = heapq.heappop(self.upper_half_min_heap)
            heapq.heappush(self.lower_half_max_heap, -val)
            
        return

    def insert(self, num: int) -> None:
        # insert new number into the right heap and rebalance
        # rebalance method takes care of checking if rebalancing is needed at all
        if not self.lower_half_max_heap or num <= -self.lower_half_max_heap[0]:
            heapq.heappush(self.lower_half_max_heap, -num)
        else:
            heapq.heappush(self.upper_half_min_heap, num)

        self._rebalance_heaps()
        return

    def get_median(self) -> float:
        # return current median in O(1) time
        if not self.lower_half_max_heap and not self.upper_half_min_heap:
            raise ValueError("Stream is Empty.")

        if len(self.lower_half_max_heap) == len(self.upper_half_min_heap):
            lower_max = - self.lower_half_max_heap[0]
            upper_min = self.upper_half_min_heap[0]
            return (lower_max + upper_min) / 2.0
        
        return float(-self.lower_half_max_heap[0])

# =====================================================================
# TEST SUITE
# =====================================================================
class TestContinuousMedian(unittest.TestCase):

    def test_01_empty_stream_raises_error(self):
        """Querying median on empty data structure raises ValueError."""
        finder = ContinuousMedian()
        with self.assertRaises(ValueError):
            finder.get_median()

    def test_02_single_element(self):
        """Single element returns itself as median."""
        finder = ContinuousMedian()
        finder.insert(5)
        self.assertEqual(finder.get_median(), 5.0)

    def test_03_even_number_of_elements(self):
        """Even count of elements calculates average of two central values."""
        finder = ContinuousMedian()
        finder.insert(1)
        finder.insert(2)
        self.assertEqual(finder.get_median(), 1.5)

    def test_04_odd_number_of_elements(self):
        """Odd count of elements returns middle element."""
        finder = ContinuousMedian()
        for num in [1, 2, 3]:
            finder.insert(num)
        self.assertEqual(finder.get_median(), 2.0)

    def test_05_unordered_stream_sequence(self):
        """Stream inserted in arbitrary order tracks median correctly at each step."""
        finder = ContinuousMedian()
        expected_medians = [10, 15.0, 10, 9.0, 10]
        actual_medians = []

        for num in [10, 20, 5, 8, 12]:
            finder.insert(num)
            actual_medians.append(finder.get_median())

        self.assertEqual(actual_medians, expected_medians)

    def test_06_duplicates_and_negatives(self):
        """Handles negative numbers and duplicate stream values correctly."""
        finder = ContinuousMedian()
        for num in [-5, -10, -5, 0]:
            finder.insert(num)
        self.assertEqual(finder.get_median(), -5.0)


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.20 - Continuous Median\n{'='*75}")

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
    run_tests(TestContinuousMedian)