import unittest

# Optimal - working
    # optimal for single query linear scan
def find_closest_distance(words: list[str], word1: str, word2: str) -> int:
    # Time: O(N)
    # SpacE: O(1)

    last_p1, last_p2 = -1, -1
    min_dist = float("inf")

    for i, word in enumerate(words):
        if word == word1:
            last_p1 = i
            if last_p2 != -1:
                min_dist = min(min_dist, last_p1 - last_p2)
        elif word == word2:
            last_p2 = i
            if last_p1 != -1:
                min_dist = min(min_dist, last_p2 - last_p1)

    return min_dist if min_dist != float("inf") else -1

class WordDistance:
    # Precomputed Solution for repeated queries
    def __init__(self, words: list[str]):
        self.locations: dict[str, list[int]] = {}
        # words, and sorted list of indices
        self._preprocess(words)

    def _preprocess(self, words: list[str]) -> None:
        # helper, build locations hash map 
        for i, word in enumerate(words):
            self.locations.setdefault(word, []).append(i)

    def _find_min_distance_2_ptr(self, list1: list[int], list2: list[int]) -> int:
        # helper compute minimum index difference, from 2 sorted lists
        p1 = p2 = 0
        min_dist = float("inf")

        while p1 < len(list1) and p2 < len(list2):
            v1, v2 = list1[p1], list2[p2]
            min_dist = min(min_dist, abs(v1 - v2))

            if v1 < v2:
                p1 += 1
            else:
                p2 += 1

        return min_dist

    def find_closest_distance(self, word1: str, word2: str) -> int:
        # Time per query: O(L1 + L2)
        # Space: O(N) for precomputed hash map
        if word1 not in self.locations or word2 not in self.locations:
            return -1

        list1 = self.locations[word1]
        list2 = self.locations[word2]
        return self._find_min_distance_2_ptr(list1, list2)

# =====================================================================
# TEST SUITE
# =====================================================================
class TestWordDistance(unittest.TestCase):

    def test_01_empty_words_list(self):
        """Empty words list returns -1."""
        self.assertEqual(find_closest_distance([], "cat", "dog"), -1)

    def test_02_word_not_in_list(self):
        """Word missing from list returns -1."""
        words = ["the", "quick", "brown", "fox"]
        self.assertEqual(find_closest_distance(words, "cat", "fox"), -1)

    def test_03_adjacent_words(self):
        """Adjacent target words return distance of 1."""
        words = ["the", "quick", "brown", "fox"]
        self.assertEqual(find_closest_distance(words, "quick", "brown"), 1)

    def test_04_multiple_occurrences_closest_pair(self):
        """Selects closest occurrence pair among multiple occurrences."""
        words = ["a", "b", "c", "d", "a", "e", "b"]
        self.assertEqual(find_closest_distance(words, "a", "b"), 1)

    def test_05_words_at_extremes(self):
        """Target words positioned at start and end of list."""
        words = ["first", "middle1", "middle2", "last"]
        self.assertEqual(find_closest_distance(words, "first", "last"), 3)

# =====================================================================
# TEST SUITE (DIRECT CLASS TESTING)
# =====================================================================
class TestWordDistanceClass(unittest.TestCase):

    def test_01_empty_words_list(self):
        """Empty words list returns -1 for any query."""
        wd = WordDistance([])
        self.assertEqual(wd.find_closest_distance("cat", "dog"), -1)

    def test_02_word_not_in_list(self):
        """Missing target word returns -1."""
        wd = WordDistance(["the", "quick", "brown", "fox"])
        self.assertEqual(wd.find_closest_distance("cat", "fox"), -1)

    def test_03_adjacent_words(self):
        """Adjacent target words return distance of 1."""
        wd = WordDistance(["the", "quick", "brown", "fox"])
        self.assertEqual(wd.find_closest_distance("quick", "brown"), 1)

    def test_04_multiple_occurrences_closest_pair(self):
        """Selects closest occurrence pair among multiple occurrences."""
        wd = WordDistance(["a", "b", "c", "d", "a", "e", "b"])
        self.assertEqual(wd.find_closest_distance("a", "b"), 1)

    def test_05_words_at_extremes(self):
        """Target words positioned at start and end of list."""
        wd = WordDistance(["first", "middle1", "middle2", "last"])
        self.assertEqual(wd.find_closest_distance("first", "last"), 3)

    def test_06_repeated_queries_same_instance(self):
        """Verifies multiple query calls on a single preprocessed instance."""
        words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
        wd = WordDistance(words)

        self.assertEqual(wd.find_closest_distance("quick", "fox"), 2)
        self.assertEqual(wd.find_closest_distance("the", "dog"), 2)
        self.assertEqual(wd.find_closest_distance("brown", "lazy"), 5)

# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.11 - Word Distance\n{'='*75}")

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
    run_tests(TestWordDistance)
    run_tests(TestWordDistanceClass)