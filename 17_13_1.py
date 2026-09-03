import unittest

# SOLUTION 1 - OPTIMAL
# converting given dictionary of words into prefix-trie
# preventing unnecessary checks for subsequent substring from an index

class TrieNode:
    # base node for prefic search tree
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    # Prefix TRee - speeding the string word matching

    def __init__(self, dictionary: set[str]):
        self.root = TrieNode()
        for word in dictionary:
            self.insert(word)

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char] # move to next character, like incrementing
        node.is_word = True # Flag marking end of a word

def respace(dictionary: set[str], sentence: str) -> int:
    # Optimal solution: Bottom up DP with Trie Lookups
    # Time complexity O(N ^ 2), worst case, heavily optimised with Trie Pruning
    # Auxiliary space O(N + total_dict_characters)

    if not sentence:
        return 0

    n = len(sentence)
    trie = Trie(dictionary)
    dp = [0] * (n + 1)

    # solve from right to left
    # as like other string manipulation problems
    for  i in range(n - 1, -1, -1):
        # case 1: default Option treat sentence[i] character as unparseable
        best = 1 + dp[i + 1]

        # Case 2: treat sentence[i] as start to a valid word, 
        curr_node = trie.root
        for j in range(i, n):
            char = sentence[j]
            if char not in curr_node.children:
                break # Early pruning: no words with this prefix
            
            curr_node = curr_node.children[char]
            if curr_node.is_word: # end of valid word found sentence[i : j+1]
                best = min(best, dp[j + 1])
                
        dp[i] = best

    return dp[0]

# =====================================================================
# TEST SUITE
# =====================================================================
class TestReSpace(unittest.TestCase):

    def test_01_empty_sentence(self):
        """Empty sentence returns 0 unrecognised characters."""
        self.assertEqual(respace({"cat", "dog"}, ""), 0)

    def test_02_empty_dictionary(self):
        """Empty dictionary leaves all characters unrecognised."""
        self.assertEqual(respace(set(), "hello"), 5)

    def test_03_perfect_match(self):
        """Sentence completely made of valid dictionary words returns 0 unrecognised."""
        dictionary = {"brother", "like", "my", "i"}
        self.assertEqual(respace(dictionary, "ilike mybrother"), 1)  # Space char unrecognised

    def test_04_ctci_example(self):
        """CTCI example: 'jesslookedliketimherbrother' -> 7 unrecognised chars."""
        dictionary = {"looked", "just", "like", "her", "brother"}
        sentence = "jesslookedliketimherbrother"
        self.assertEqual(respace(dictionary, sentence), 7)

    def test_05_overlapping_dictionary_words(self):
        """DP chooses longer matching words to minimize unrecognised count."""
        dictionary = {"a", "app", "apple", "pie"}
        self.assertEqual(respace(dictionary, "applepie"), 0)

    def test_06_no_matching_words(self):
        """No words match, returning full string length."""
        dictionary = {"cat", "dog"}
        self.assertEqual(respace(dictionary, "xyz"), 3)


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.13 - Re-Space\n{'='*75}")

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
    run_tests(TestReSpace)