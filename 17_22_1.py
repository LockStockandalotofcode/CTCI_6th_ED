from collections import deque, defaultdict
import unittest
from typing import Optional, List

def _build_wildcard_dict_map(dictionary: set[str], word_length: int) -> dict[str, list[str]]:
    # helper: Groups dictionary words by single character wildcard patterms
    wildcard_map = defaultdict(list)
    for word in dictionary:
        for i in range(word_length):
            pattern = word[ : i] + "*" + word[i+1 : ]
            wildcard_map[pattern].append(word)
    return wildcard_map

def find_word_path(start_word: str, end_word: str, dictionary: set[str]) -> Optional[List[str]]:
    # Standard BFS with parent tracking, ie. all visited nodes
    # Time: O(N * L), Space: O(N * L)

    if start_word not in dictionary or end_word not in dictionary or len(start_word) != len(end_word):
        return []

    word_len = len(start_word)
    wildcard_map = _build_wildcard_dict_map(dictionary, word_len)

    queue = deque([start_word])
    visited = {start_word : None} # Mapping word to its parent word

    while queue:
        curr = queue.popleft()

        if curr == end_word:
            # reconstruct path, need to traverse backwards
            path = []
            while curr is not None:
                path.append(curr)
                curr = visited[curr]
            return path[::-1]

        for i in range(word_len):
            pattern = curr[: i] + "*" + curr[i + 1 :]
            for neighbor in wildcard_map[pattern]:
                if neighbor not in visited:
                    visited[neighbor] = curr
                    queue.append(neighbor)

    return []

# =====================================================================
# TEST SUITE
# =====================================================================
class TestWordTransformer(unittest.TestCase):

    def test_01_start_equals_end(self):
        """Start word equals end word returns single-element path."""
        self.assertEqual(find_word_path("cat", "cat", {"cat"}), ["cat"])

    def test_02_different_word_lengths(self):
        """Different length words cannot be transformed, returns empty path."""
        self.assertEqual(find_word_path("cat", "cats", {"cat", "cats"}), [])

    def test_03_end_word_not_in_dictionary(self):
        """End word not present in dictionary returns empty path."""
        self.assertEqual(find_word_path("cat", "dog", {"cat", "cot", "dot"}), [])

    def test_04_direct_one_step_transformation(self):
        """Direct 1-character difference transformation."""
        dictionary = {"cat", "bat"}
        self.assertEqual(find_word_path("cat", "bat", dictionary), ["cat", "bat"])

    def test_05_multi_step_valid_path(self):
        """Multi-step path from DAMP to LIKE."""
        dictionary = {"damp", "lamp", "limp", "lime", "like"}
        path = find_word_path("damp", "like", dictionary)
        self.assertEqual(path, ["damp", "lamp", "limp", "lime", "like"])

    def test_06_no_path_exists_disconnected_graph(self):
        """No connected path between start and end word in dictionary graph."""
        dictionary = {"damp", "lamp", "like"}
        self.assertEqual(find_word_path("damp", "like", dictionary), [])


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.22 - Word Transformer\n{'='*75}")

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
    run_tests(TestWordTransformer)