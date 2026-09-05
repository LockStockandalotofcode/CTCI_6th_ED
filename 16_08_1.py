import unittest

_ONES = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
_TEENS = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
_TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
_BIGS = ["", "Thousand", "Million", "Billion"]

def _convert_three_digits(num: int) -> str:
    # Helper: converts any number between 1 and 999, to english words
    parts = []

    # find hundreds place
    if num >= 100:
        parts.append(_ONES[num // 100])
        parts.append("Hundred")
        num %= 100

    # find teens, if existing, since they are special
    # if not teen, decode tens and ones place
    if 10 <= num and num < 20:
        parts.append(_TEENS[num - 10])
    else:
        if num >= 20:
            parts.append(_TENS[num // 10])
            num %= 10
        if num >= 1:
            parts.append(_ONES[num])

    # return the string 
    return " ".join(parts)

def number_to_words(num: int) -> str:
    # Modular Chunk Processing
    # since english representation is structured into 3-digit chunks
    # Time: O(log_10 N), governed by no. of digits or no. of places
    # auxiliary space O(1)

    if num == 0:
        return "Zero"

    if num < 0:
        return "Negative" + " " + number_to_words(-num)

    chunk_count = 0
    chunks = []

    while num > 0:
        three_digit_chunk = num % 1000
        if three_digit_chunk != 0:
            translated_chunk = _convert_three_digits(three_digit_chunk)
            big_label = _BIGS[chunk_count]

            if big_label: # non-empty, or more than thousand
                chunks.append(translated_chunk + " " + big_label)
            else:
                chunks.append(translated_chunk)

        num //= 1000
        chunk_count += 1

    # reverse chunks since we processed from smallest to largest
    chunks.reverse()
    # make str of string segments
    # breakpoint()
    return " ".join(chunks)

# =====================================================================
# TEST SUITE
# =====================================================================
class TestEnglishInt(unittest.TestCase):

    def test_01_zero(self):
        """Zero converts to 'Zero'."""
        self.assertEqual(number_to_words(0), "Zero")

    def test_02_single_digit_and_teens(self):
        """Single digits and teens numbers."""
        self.assertEqual(number_to_words(5), "Five")
        self.assertEqual(number_to_words(13), "Thirteen")

    def test_03_tens_and_hundreds(self):
        """Compound tens and hundreds."""
        self.assertEqual(number_to_words(42), "Forty Two")
        self.assertEqual(number_to_words(105), "One Hundred Five")
        self.assertEqual(number_to_words(999), "Nine Hundred Ninety Nine")

    def test_04_thousands_and_million(self):
        """Thousands and Millions places formatting."""
        self.assertEqual(number_to_words(1000), "One Thousand")
        self.assertEqual(number_to_words(1234567), "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")
        
    def test_05_negative_numbers(self):
        """Handles negative integers."""
        self.assertEqual(number_to_words(-12), "Negative Twelve")


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.8 - English Int\n{'='*75}")

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
    run_tests(TestEnglishInt)