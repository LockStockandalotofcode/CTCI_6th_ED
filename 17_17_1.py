import unittest

class TrieNode:
    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.word_ends: list[str] = []

def _build_trie(small_words: list[str]) -> TrieNode:
    # build trie of small words
    root = TrieNode()
    for word in small_words:
        if not word:
            continue
        curr = root
        for char in word:
            curr = curr.children.setdefault(char, TrieNode())
            # if char does not exist as children node of curr, make it a TrieNode by default
        curr.word_ends.append(word)
    return root

def multi_search(big_str: str, small_words: list[str]) -> dict[str, list[int]]:
    # Optimal 
    # Trie of small words scanned over big string
    # Time: O(B*L + S)
    # Auxiliary space: O(S)

    root = _build_trie(small_words)
    result: dict[str, list[int]] = {s: [] for s in small_words}

    def _search_from_offset(start_idx: int) -> None:
        # searches Trie starting from big_str[start_idx]
        curr = root
        for i in range(start_idx, len(big_str)):
            char = big_str[i]
            if char not in curr.children:
                break
            curr = curr.children[char] # increment, traverse to next char or child node
            for matched_word in curr.word_ends:
                result[matched_word].append(start_idx)

    for i in range(len(big_str)):
        _search_from_offset(i)

    return result

# =====================================================================
# TEST SUITE
# =====================================================================
class TestMultiSearch(unittest.TestCase):

    def test_01_empty_big_string(self):
        """Empty big string returns empty index lists for all target words."""
        small_words = ["is", "ppi"]
        self.assertEqual(
            multi_search("", small_words), {"is": [], "ppi": []}
        )

    def test_02_word_not_found(self):
        """Target words not present in big string return empty lists."""
        big = "mississippi"
        small_words = ["cat", "dog"]
        self.assertEqual(
            multi_search(big, small_words), {"cat": [], "dog": []}
        )

    def test_03_multiple_occurrences(self):
        """Finds multiple starting indices for target words."""
        big = "mississippi"
        small_words = ["is", "ppi", "hi"]
        expected = {"is": [1, 4], "ppi": [8], "hi": []}
        self.assertEqual(multi_search(big, small_words), expected)

    def test_04_overlapping_occurrences(self):
        """Tracks overlapping occurrences correctly."""
        big = "aaaa"
        small_words = ["aa"]
        expected = {"aa": [0, 1, 2]}
        self.assertEqual(multi_search(big, small_words), expected)

    def test_05_empty_word_in_small_words(self):
        """Empty target string in small words list returns empty index list."""
        big = "abc"
        small_words = [""]
        self.assertEqual(multi_search(big, small_words), {"": []})


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.17 - Multi Search\n{'='*75}")

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
    run_tests(TestMultiSearch)