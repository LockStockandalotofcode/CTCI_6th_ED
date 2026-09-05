import unittest

#### strategy
# 1. normalise pattern: ensure starts with a

# 2.
# count frequencies: of a, b
# count first index of b

# 3.
# iterate over all possible L_a values (length of substring with key a)
# For each candidate length L_a belongs in range [0, floor(L_v / c_a)]:
# 4.
# extract and verify against original value, all candidate substrings
# 5.
# return False if no valid pair found
 
def _count_pattern_chars(pattern: str) -> tuple[int, int, int]:
    # helper returns freq of a, b in pattern, and index of first b
    count_a = 0
    count_b = 0
    first_b = -1

    for i, char in enumerate(pattern):
        if char == "a":
            count_a += 1
        else:
            count_b += 1
            if first_b == -1:
                first_b = i

    return count_a, count_b, first_b

def _matches_original_value(pattern: str, value: str, str_a: str, str_b: str) -> bool:
    # helper validate candidate string, if it equals value
    val_idx = 0
    for char in pattern:
        curr = str_a if char == "a" else str_b
        curr_len = len(curr)

        # check if slice matches expected portion in value string
        if value[val_idx : val_idx + len(curr)] != curr:
            return False
        val_idx += len(curr)

    return val_idx == len(value)
 
def pattern_match(pattern: str, value: str) -> bool:
    # Linear scan over string lengths
    # Time: O(N^2 / count_a), worst case O(N^2 / count_a)
    # space: O(N)

    if not pattern:
        return not value

    if pattern[0] == 'b':
        pattern = "".join("a" if c == "b" else "b" for c in pattern)

    len_val = len(value)
    count_a, count_b, first_b_index = _count_pattern_chars(pattern)

    max_len_a = len_val // count_a if count_a > 0 else 0

    for len_a in range(max_len_a + 1):
        rem_len = len_val - (count_a * len_a)

        if count_b == 0 and rem_len == 0:
            str_a = value[ : len_a]
            if _matches_original_value(pattern, value, str_a, ""):
                return True
        elif count_b > 0 and rem_len >= 0 and rem_len % count_b == 0:
            len_b = rem_len // count_b

            # both pattern a and b must be non empty when both exist
            if len_a == 0 or len_b == 0:
                continue
            
            str_a = value[ : len_a]
            b_start_idx = first_b_index * len_a
            str_b = value[b_start_idx : b_start_idx + len_b]
            
            
            if str_a != str_b and _matches_original_value(pattern, value, str_a, str_b):
                return True

    return False


# =====================================================================
# TEST SUITE
# =====================================================================
class TestPatternMatching(unittest.TestCase):

    def test_01_valid_multi_character_pattern(self):
        """Pattern 'aabab' matching 'catcatgocatgo'."""
        self.assertTrue(pattern_match("aabab", "catcatgocatgo"))

    def test_02_repeating_single_variable_pattern(self):
        """Pattern 'aaaa' matching 'dogdogdogdog'."""
        self.assertTrue(pattern_match("aaaa", "dogdogdogdog"))

    def test_03_invalid_pattern_match(self):
        """Pattern 'aab' fails against 'xyz'."""
        self.assertFalse(pattern_match("aab", "xyz"))

    def test_04_empty_pattern_and_value(self):
        """Empty pattern matches empty value."""
        self.assertTrue(pattern_match("", ""))

    def test_05_single_character_pattern(self):
        """Pattern 'a' matches any full string."""
        self.assertTrue(pattern_match("a", "anything"))

    def test_06_value_too_short(self):
        """Value length shorter than pattern length fails."""
        self.assertFalse(pattern_match("aabab", "cat"))


# =====================================================================
# CONCISE SINGLE-LINE TEST RUNNER
# =====================================================================
def run_tests(test_class, title: str):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: {title}\n{'='*75}")

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
            err_msg = result.failures[0][1].strip().splitlines()[-1]
            print(f"  ❌ [FAIL] {desc} | Details: {err_msg}")
            failed += 1
        elif result.errors:
            err_msg = result.errors[0][1].strip().splitlines()[-1]
            print(f"  ⚠️  [ERROR] {desc} | Details: {err_msg}")
            errors += 1

    total = passed + failed + errors
    pass_rate = (passed / total * 100) if total > 0 else 0.0

    print(f"{'-'*75}")
    print(f" SUMMARY: Total: {total} | Passed: {passed} ✅ | Failed: {failed} ❌ | Errors: {errors} ⚠️ | Rate: {pass_rate:.1f}%")
    print(f"{'='*75}\n")


if __name__ == "__main__":
    run_tests(TestPatternMatching, "CTCI 16.18 - Pattern Matching")