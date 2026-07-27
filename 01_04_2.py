def palindrome_permutation(s: str) -> bool:
    # base case
    if not s:
        return True
    # turn all to  lower case
    new_s = s.lower()
    freq_table = build_char_freq_table(new_s)
    return check_max_one_odd(freq_table)

# helper functions
def build_char_freq_table(s: str) -> dict[str, int]:
    # hash table to count character frequency
    hash_table = {}
    for char in s:
        # count the frequency
        if char == " ":
            continue
        hash_table[char] = hash_table.get(char, 0) + 1

    return hash_table

def check_max_one_odd(hash_table: dict[str, int]) -> bool:
    max_odd_allowed = 0
    for _, freq in hash_table.items():
        if (freq%2) == 1:
            max_odd_allowed += 1
        
    return (max_odd_allowed <= 1)

# testing
def run_palindrome_permutation_tests():
    test_cases = [
        # (input_str, expected)
        ("", True),  # Empty string
        ("a", True),  # Single char
        ("Tact Coa", True),  # Standard CTCI example ("taco cat")
        ("code", False),  # No palindrome permutation
        ("aab", True),  # "aba"
        ("carerac", True),  # "racecar"
        ("aA bB", True),  # Case + Space handling ("aabba")
        ("No 'x' in Nixon", True),  # Complex punctuation/casing
        ("random string", False),  # Non-palindrome
        ("aabbccdd", True),  # All even counts
        ("aabbccdde", True),  # All even + 1 odd
        ("aabbccddef", False),  # Multiple odd counts
    ]

    passed, failed = 0, 0
    print("\n" + "=" * 60)
    print("RUNNING CTCI 1.4: PALINDROME PERMUTATION TESTS")
    print("=" * 60)

    for i, (s, expected) in enumerate(test_cases, 1):
        try:
            res = palindrome_permutation(s)
            assert (
                res == expected
            ), f"Expected {expected}, got {res} for input '{s}'"
            print(f"  [PASS] Test {i:02d}: '{s}' -> {res}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: '{s}' -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"1.4 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_palindrome_permutation_tests()