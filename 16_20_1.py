import unittest

T9_MAP = {
    '2': {'a', 'b', 'c'},
    '3': {'d', 'e', 'f'},
    '4': {'g', 'h', 'i'},
    '5': {'j', 'k', 'l'},
    '6': {'m', 'n', 'o'},
    '7': {'p', 'q', 'r', 's'},
    '8': {'t', 'u', 'v'},
    '9': {'w', 'x', 'y', 'z'},
}

CHAR_TO_DIGIT = {char : digit for digit, chars in T9_MAP.items() for char in chars}

def _word_to_digits(word: str) -> str:
    # converts a word into corresponding T9 digits attached string
    return "".join(
        CHAR_TO_DIGIT[char.lower()] 
        for char in word 
        if char.lower() in CHAR_TO_DIGIT
        ) 

class T9DictionaryOptimal:
    # Precomputed hash map for O(1) lookups
    def __init__(self, dictionary: list[str] | set[str]):
        # breakpoint()
        self.t9_index: dict[str, list[str]] = {}
        self._build_index(dictionary)

    def _build_index(self, dictionary: list[str]) -> None:
        # populate hash table with digit -> word mappings
        for word in dictionary:
            digit_seq = _word_to_digits(word)
            if digit_seq not in self.t9_index:
                self.t9_index[digit_seq] = []
            self.t9_index[digit_seq].append(word)

    def get_valid_words(self, digits: str) -> list[str]:
        # breakpoint()
        if not digits or len(self.t9_index) == 0:
            return []
        # returns all valid words mapped to this digits combination
        return sorted(self.t9_index.get(digits, []))





# # =====================================================================
# # SOLUTION PLACEHOLDER
# # Replace or import your actual function here
# # =====================================================================
# def t9.get_valid_words(digits: str, dictionary: set[str]) -> list[str]:
#     """Returns all words from dictionary matching the given T9 key sequence."""
#     if not digits or not dictionary:
#         return []

#     results = []
#     for word in dictionary:
#         if len(word) != len(digits):
#             continue
#         match = True
#         for char, digit in zip(word.lower(), digits):
#             if digit not in T9_MAP or char not in T9_MAP[digit]:
#                 match = False
#                 break
#         if match:
#             results.append(word)

#     return sorted(results)


# =====================================================================
# TEST SUITE
# =====================================================================
class TestT9(unittest.TestCase):

    def test_01_empty_digits(self):
        """Empty digit sequence returns empty list."""
        t9 = T9DictionaryOptimal({"tree", "used"})
        self.assertEqual(t9.get_valid_words(""), [])

    def test_02_empty_dictionary(self):
        """Empty dictionary returns empty list."""
        t9 = T9DictionaryOptimal( set())
        self.assertEqual(t9.get_valid_words("8733"), [])

    def test_03_standard_t9_matches(self):
        """Digit sequence 8733 matches both 'tree' and 'used'."""
        dictionary = {"tree", "used", "cool", "apply"}
        t9 = T9DictionaryOptimal( dictionary)
        self.assertEqual(t9.get_valid_words("8733"), ["tree", "used"])

    def test_04_no_matching_words(self):
        """Valid digits but no matching words in dictionary."""
        dictionary = {"hello", "world"}
        t9 = T9DictionaryOptimal( dictionary)
        self.assertEqual(t9.get_valid_words("9999"), [])

    def test_05_word_length_mismatch(self):
        """Ignores dictionary words of different lengths."""
        dictionary = {"a", "at", "tree"}
        t9 = T9DictionaryOptimal( dictionary)
        self.assertEqual(t9.get_valid_words("28"), ["at"])

    def test_06_case_insensitivity(self):
        """Matches dictionary words regardless of casing."""
        dictionary = {"Tree", "USED"}
        t9 = T9DictionaryOptimal( dictionary)
        self.assertEqual(t9.get_valid_words("8733"), ["Tree", "USED"])


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.20 - T9\n{'='*75}")

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
    print(
        f" SUMMARY: Total: {total} | Passed: {passed} ✅ | Failed: {failed} ❌ | Errors: {errors} ⚠️ | Rate: {pass_rate:.1f}%"
    )
    print(f"{'='*75}\n")


if __name__ == "__main__":
    run_tests(TestT9)