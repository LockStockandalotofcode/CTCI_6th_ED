import heapq
import unittest
from typing import Optional, List
from collections import defaultdict

def shortest_supersequence(shorter: list[int], longer: list[int]) -> Optional[list[int]]:
    if not shorter or not longer or len(shorter) > len(longer):
        return []

    target_set = set(shorter)

    # STEP 1: build lists of indices for each element of shorter array
    locations = defaultdict(list)
    for idx, val in enumerate(longer):
        if val in target_set:
            locations[val].append(idx)

    # early return if any element of shorter array is not present in longer array
    if len(locations) < len(target_set):
        return []

    # STEP 2: Initialise heap with first index of each list
    min_heap = []
    max_val = -1

    for item in target_set:
        first_idx = locations[item][0]
        # Store tuple : (index_in_longer_arr, list_key, index_in_locations_list)
        heapq.heappush(min_heap, (first_idx, item, 0))
        max_val = max(max_val, first_idx)

    best_range= None
    min_len = float("inf")
    # STEP 3: Process heap
    while True:
        # pop the top of heap
        min_idx, item, list_idx = heapq.heappop(min_heap)

        # check current range, if length of this window is less than min window, update
        current_len = max_val - min_idx + 1
        if current_len < min_len:
            min_len = current_len
            best_range = [min_idx, max_val]

        # if the locations list for any item has been exhausted, we stop further execution
        if list_idx >= len(locations[item]) - 1:
            break

        # INCREMENT STEP of loop
        # push next index from the same list into heap, for next iteration, to check all valid windows
        next_idx = locations[item][list_idx + 1]
        heapq.heappush(min_heap, (next_idx, item, list_idx + 1))
        max_val = max(max_val, next_idx)

    return best_range

# # =====================================================================
# # SOLUTION PLACEHOLDER
# # Replace or import your actual function here
# # =====================================================================
# def shortest_supersequence(smaller: list[int], longer: list[int]) -> list[int]:
#     """Finds the shortest subarray in `longer` containing all elements of `smaller`.
#     Returns [start, end] inclusive, or [] if no valid supersequence exists.
#     """
#     if not smaller or not longer or len(smaller) > len(longer):
#         return []

#     target_set = set(smaller)
#     needed = len(target_set)

#     counts = {}
#     matched = 0

#     min_len = float("inf")
#     best_range = []

#     left = 0
#     for right in range(len(longer)):
#         val = longer[right]
#         if val in target_set:
#             counts[val] = counts.get(val, 0) + 1
#             if counts[val] == 1:
#                 matched += 1

#         while matched == needed:
#             current_len = right - left + 1
#             if current_len < min_len:
#                 min_len = current_len
#                 best_range = [left, right]

#             left_val = longer[left]
#             if left_val in target_set:
#                 counts[left_val] -= 1
#                 if counts[left_val] == 0:
#                     matched -= 1
#             left += 1

#     return best_range


# =====================================================================
# TEST SUITE
# =====================================================================
class TestShortestSupersequence(unittest.TestCase):

    def test_01_empty_smaller_or_longer(self):
        """Empty inputs return empty list."""
        self.assertEqual(shortest_supersequence([], [1, 2, 3]), [])
        self.assertEqual(shortest_supersequence([1, 2], []), [])

    def test_02_smaller_longer_than_longer(self):
        """`smaller` array longer than `longer` returns empty list."""
        self.assertEqual(shortest_supersequence([1, 2, 3], [1, 2]), [])

    def test_03_elements_missing(self):
        """When not all items in `smaller` exist in `longer`."""
        self.assertEqual(shortest_supersequence([1, 5], [1, 2, 3, 4]), [])

    def test_04_exact_match(self):
        """Exact match size returns full bounds."""
        self.assertEqual(shortest_supersequence([1, 2], [1, 2]), [0, 1])

    def test_05_ctci_example(self):
        """CTCI example: smaller=[1, 5, 9], longer=[7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7] -> [7, 10]."""
        smaller = [1, 5, 9]
        longer = [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7]
        self.assertEqual(shortest_supersequence(smaller, longer), [7, 10])

    def test_06_duplicates_in_longer(self):
        """Handles duplicates inside sliding window cleanly."""
        smaller = [1, 2]
        longer = [1, 1, 1, 2]
        self.assertEqual(shortest_supersequence(smaller, longer), [2, 3])

    def test_07_single_element_smaller(self):
        """Single element target finds first occurrence."""
        self.assertEqual(shortest_supersequence([3], [1, 2, 3, 4]), [2, 2])


# =====================================================================
# INFORMATIVE TEST RUNNER
# =====================================================================
def run_informative_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.18 - Shortest Supersequence\n{'='*75}")

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
    print(f" EXECUTION SUMMARY:")
    print(f" Total Tests : {total}")
    print(f" Passed      : {passed} ✅")
    print(f" Failed      : {failed} ❌")
    print(f" Errors      : {errors} ⚠️")
    print(f" Success Rate: {pass_rate:.1f}%")
    print(f"{'='*75}\n")


if __name__ == "__main__":
    run_informative_tests(TestShortestSupersequence)