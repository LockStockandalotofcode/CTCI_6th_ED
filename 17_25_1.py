import unittest
from collections import defaultdict


class TrieNode:
    """Node representation for Prefix Tree (Trie)."""

    def __init__(self):
        self.children: dict[str, "TrieNode"] = {}
        self.is_word = False


class Trie:
    """Prefix Tree supporting prefix and full-word validation."""

    def __init__(self, words: list[str]):
        self.root = TrieNode()
        for w in words:
            self.insert(w)

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            curr = curr.children.setdefault(char, TrieNode())
        curr.is_word = True

    def contains_prefix(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return True

    def contains_word(self, word: str) -> bool:
        curr = self.root
        for char in word:
            if char not in curr.children:
                return False
            curr = curr.children[char]
        return curr.is_word


def _get_column_prefix(grid: list[str], col_idx: int) -> str:
    """Helper to construct vertical column string up to the current row."""
    return "".join(row[col_idx] for row in grid)


def _search_rectangle(
    height: int,
    width: int,
    current_grid: list[str],
    candidate_words: list[str],
    col_trie: Trie,
) -> list[str] | None:
    """Backtracking helper to construct a valid word rectangle of size height x width."""
    if len(current_grid) == height:
        for c in range(width):
            col_str = _get_column_prefix(current_grid, c)
            if not col_trie.contains_word(col_str):
                return None
        return list(current_grid)

    for word in candidate_words:
        current_grid.append(word)

        valid_prefixes = True
        for c in range(width):
            col_prefix = _get_column_prefix(current_grid, c)
            if not col_trie.contains_prefix(col_prefix):
                valid_prefixes = False
                break

        if valid_prefixes:
            res = _search_rectangle(
                height, width, current_grid, candidate_words, col_trie
            )
            if res:
                return res

        current_grid.pop()

    return None


def max_word_rectangle(words: list[str]) -> list[str]:
    """Finds the largest rectangle of letters such that every row forms a valid word

    (reading left-to-right) and every column forms a valid word (reading top-to-bottom).
    """
    if not words:
        return []

    # Sort deduplicated words to ensure deterministic exploration order
    unique_words = sorted(list(set(words)))

    words_by_length: dict[int, list[str]] = defaultdict(list)
    for w in unique_words:
        words_by_length[len(w)].append(w)

    tries_by_length: dict[int, Trie] = {
        length: Trie(w_list) for length, w_list in words_by_length.items()
    }

    length_keys = list(words_by_length.keys())
    dimension_pairs: list[tuple[int, int, int]] = []

    for h in length_keys:
        for w in length_keys:
            dimension_pairs.append((h * w, h, w))

    # Sort descending by area; break ties by height to prioritize larger dimensions
    dimension_pairs.sort(key=lambda x: (x[0], x[1]), reverse=True)

    for area, h, w in dimension_pairs:
        row_candidates = words_by_length[w]
        col_trie = tries_by_length[h]

        result = _search_rectangle(h, w, [], row_candidates, col_trie)
        if result:
            return result

    return []


# =====================================================================
# TEST SUITE
# =====================================================================
class TestWordRectangle(unittest.TestCase):

    def _assert_valid_rectangle(self, grid: list[str], word_list: list[str]):
        """Helper to verify both rows and columns form valid words from word_list."""
        self.assertIsNotNone(grid)
        self.assertGreater(len(grid), 0)
        word_set = set(word_list)
        height = len(grid)
        width = len(grid[0])

        # Check rows
        for row in grid:
            self.assertEqual(len(row), width)
            self.assertIn(row, word_set)

        # Check columns
        for c in range(width):
            col_str = "".join(grid[r][c] for r in range(height))
            self.assertIn(col_str, word_set)

    def test_01_empty_word_list(self):
        """Empty input word list returns empty rectangle."""
        self.assertEqual(max_word_rectangle([]), [])

    def test_02_single_letter_words(self):
        """Single character words form valid rectangle."""
        words = ["a", "b"]
        res = max_word_rectangle(words)
        self.assertEqual(len(res), 1)
        self.assertEqual(len(res[0]), 1)

    def test_03_valid_2x2_word_rectangle(self):
        """Constructs valid 2x2 word rectangle where rows and columns form valid words."""
        words = ["at", "to", "an", "on"]
        res = max_word_rectangle(words)
        self.assertEqual(len(res), 2)
        self.assertEqual(len(res[0]), 2)
        self._assert_valid_rectangle(res, words)

    def test_04_no_valid_rectangle_possible(self):
        """Returns empty list when no valid cross-word rectangle can be formed."""
        words = ["xyz", "abc", "mno"]
        self.assertEqual(max_word_rectangle(words), [])

    def test_05_maximizes_total_area(self):
        """Selects 3x3 rectangle layout maximizing total area over smaller ones."""
        words = ["cat", "ate", "tea", "c", "a", "t"]
        res = max_word_rectangle(words)
        self.assertEqual(len(res), 3)
        self.assertEqual(len(res[0]), 3)
        self._assert_valid_rectangle(res, words)

    def test_06_asymmetric_rectangle_3x2(self):
        """Validates asymmetric word rectangle (3 rows x 2 columns)."""
        words = ["at", "to", "so", "ats", "too"]
        res = max_word_rectangle(words)
        self.assertEqual(len(res), 3)
        self.assertEqual(len(res[0]), 2)
        self._assert_valid_rectangle(res, words)

    def test_07_duplicate_input_words(self):
        """Handles duplicate words in input gracefully without infinite loops."""
        words = ["at", "at", "to", "to", "an", "on"]
        res = max_word_rectangle(words)
        self.assertEqual(len(res), 2)
        self.assertEqual(len(res[0]), 2)
        self._assert_valid_rectangle(res, words)


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.25 - Word Rectangle\n{'='*75}")

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
    run_tests(TestWordRectangle)