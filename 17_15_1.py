import unittest

def _can_build_word(word: str, is_original_word: bool, word_map: dict[str, bool]) -> bool:
    # Top-down recursive checking 
    # if word can be formed by other list words

    # Base Case
    if word in word_map and not is_original_word:
        return True
        
    # split the word, check if the slices exist in word_map
    for i in range(1, len(word)):
        left_slice = word[ : i]
        right_slice = word[i : ]

        if left_slice in word_map and word_map[left_slice]:
            # left_slice is an existing word 
            if _can_build_word(right_slice, False, word_map):
                return True

    # memoisation
    word_map[word] = False
    # some words that are not composite of other words
    # since this is recursive, smaller non-composite words get hashed
    return False
        

def find_longest_composite_word(words: list[str]) -> str:
    if not words:
        return ""

    # build word_map for O(1) lookup
    word_map = {word: True for word in words}

    # Sort by decreasing length, the original array
    sorted_words = sorted(words, key=len, reverse=True)

    for word in sorted_words:
        if _can_build_word(word, True, word_map):
            return word

    return ""
        
# =====================================================================
# TEST SUITE
# =====================================================================
class TestLongestWord(unittest.TestCase):

    def test_01_empty_words_list(self):
        """Empty input list returns empty string."""
        self.assertEqual(find_longest_composite_word([]), "")

    def test_02_no_composite_words(self):
        """List with no formable composite words returns empty string."""
        words = ["cat", "dog", "banana"]
        self.assertEqual(find_longest_composite_word(words), "")

    def test_03_standard_composite_word(self):
        """Finds 'dogwalker' formed by 'dog' + 'walker'."""
        words = ["dog", "walker", "dogwalker", "walk"]
        self.assertEqual(find_longest_composite_word(words), "dogwalker")

    def test_04_multiple_smaller_components(self):
        """Finds composite word built from 3 distinct smaller words."""
        words = ["a", "b", "c", "ab", "abc", "bc"]
        self.assertEqual(find_longest_composite_word(words), "abc")

    def test_05_tiebreaker_alphabetical(self):
        """Ties in longest length pick the lexicographically smaller word."""
        words = ["cat", "dog", "catdog", "dogcat"]
        self.assertEqual(find_longest_composite_word(words), "catdog")


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.15 - Longest Word\n{'='*75}")

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
    run_tests(TestLongestWord)