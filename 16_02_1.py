import re
import unittest

class WordFrequencyTracker:
    # Precomputes word for frequencies for repetitive O(1) lookups
    # Precompuation time: O(N), Query Time: O(1), Space: O(N)
    
    def __init__(self, book: list[str]):
        self.freq_map = {}
        self._build_freq_map(book)

    def _normalise_string(self, word: str) -> str:
        # helper method to strip non-alphanumerix characters and convert to lowercase
        # Strip non-alpphanumeric characters and convert to lowercase
        return re.sub(r"[^\w]", "", word.lower())

    def _build_freq_map(self, book: list[str]) -> None:
        # helper method to populate hash map with book tokens

        # supports both full text string and a pre-tokenised string
        tokens = book.split() if isinstance(book, str) else book
        for token in tokens:
            clean_word = self._normalise_string(token)
            if clean_word:
                self.freq_map[clean_word] = self.freq_map.get(clean_word, 0) + 1

    def get_frequency(self, query_word: str) -> int:
        # breakpoint()
        # lookup time O(1)
        clean_query = self._normalise_string(query_word)
        return self.freq_map.get(clean_query, 0)

# def word_freq_single_query(book: list[str], query_word: str) -> int:
#     # Single freqsuency approach without precomputation
#     # Time O(N), Space: O(1)

#     clean_query = re.sub(r"[^a-zA-Z0-9]", "", query_word).lower()
#     count = 0

#     for token in book:
#         clean_token =  re.sub(r"[^a-zA-Z0-9]", "", token).lower()
#         if clean_token == clean_query:
#             count += 1

#     return count

# # =====================================================================
# # SOLUTION PLACEHOLDER
# # Replace or import your actual class/function here
# # =====================================================================
# class WordFrequencyTracker:
#     """Preprocesses a text body to allow O(1) frequency lookups per query."""

#     def __init__(self, text: str):
#         self.freq_map = {}
#         if text:
#             cleaned_text = re.sub(r"[^\w\s]", "", text.lower())
#             for word in cleaned_text.split():
#                 self.freq_map[word] = self.freq_map.get(word, 0) + 1

#     def get_frequency(self, word: str) -> int:
#         if not word or not word.strip():
#             return 0
#         cleaned_word = re.sub(r"[^\w\s]", "", word.lower().strip())
#         return self.freq_map.get(cleaned_word, 0)


# =====================================================================
# TEST SUITE
# =====================================================================
class TestWordFrequencies(unittest.TestCase):

    def test_01_empty_book_text(self):
        """Empty book text returns 0 frequency for any word query."""
        tracker = WordFrequencyTracker("")
        self.assertEqual(tracker.get_frequency("hello"), 0)

    def test_02_case_insensitivity(self):
        """Query matching is case-insensitive ('The' matches 'the')."""
        tracker = WordFrequencyTracker("The book is on the table.")
        self.assertEqual(tracker.get_frequency("the"), 2)
        self.assertEqual(tracker.get_frequency("THE"), 2)

    def test_03_punctuation_stripping(self):
        """Punctuation attached to words is stripped during frequency count."""
        text = "Hello, world! Hello... world?"
        tracker = WordFrequencyTracker(text)
        self.assertEqual(tracker.get_frequency("hello"), 2)
        self.assertEqual(tracker.get_frequency("world"), 2)

    def test_04_word_not_present(self):
        """Query for a non-existent word returns 0."""
        tracker = WordFrequencyTracker("Quick brown fox jumps over lazy dog.")
        self.assertEqual(tracker.get_frequency("cat"), 0)

    def test_05_whitespace_and_empty_queries(self):
        """Empty string or whitespace queries return 0."""
        tracker = WordFrequencyTracker("Some standard text here.")
        self.assertEqual(tracker.get_frequency(""), 0)
        self.assertEqual(tracker.get_frequency("   "), 0)


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.2 - Word Frequencies\n{'='*75}")

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
    run_tests(TestWordFrequencies)