def check_permutation(str1: str, str2: str) -> bool:
    if not str1 and not str2:
        return True
    if not str1 or not str2:
        return False
    
    # hash set- not a good idea, since python sets dont store duplicate values
    hash_table = {} # char: freq
    # we traverse str1, add all its elements to dict
    # then we traverse str2, remove all its elements to dict
    # if nothing remains, they are, otherwise they're not
    for char in str1:
        hash_table[char] = hash_table.get(char, 0) + 1

    for char in str2:
        if char not in hash_table or hash_table[char] == 0:
            return False
        hash_table[char] -= 1
        
    for key, val in hash_table.items():
        if val != 0:
            return False

    return True



























def run_check_permutation_tests():
    test_cases = [
        # (str1, str2, expected)
        # 1. Empty & Single Character Cases
        ("", "", True),
        ("a", "a", True),
        ("a", "b", False),
        # 2. Length Mismatch
        ("abc", "ab", False),
        ("a", "", False),
        # 3. Exact Matches & Valid Permutations
        ("god", "dog", True),
        ("listen", "silent", True),
        ("aab", "aba", True),
        # 4. Same Characters, Wrong Counts
        ("aab", "abb", False),
        ("aaab", "aabb", False),
        # 5. Case & Whitespace Sensitivity (Standard Strict Assumptions)
        ("God", "dog", False),  # Case sensitive
        ("god ", "dog", False),  # Whitespace sensitive
        ("  ", "  ", True),
        ("a b c", "c b a", True),
    ]

    passed = 0
    failed = 0
    print("\n" + "=" * 60)
    print("RUNNING CTCI 1.2: CHECK PERMUTATION TESTS")
    print("=" * 60)

    for i, (str1, str2, expected) in enumerate(test_cases, 1):
        try:
            result = check_permutation(str1, str2)
            assert (
                result == expected
            ), f"Expected {expected}, got {result} for ('{str1}', '{str2}')"
            print(f"  [PASS] Test {i:02d}: ('{str1}', '{str2}') -> {result}")
            passed += 1
        except Exception as e:
            print(
                f"  [FAIL] Test {i:02d}: ('{str1}', '{str2}') -> ERROR: {e}"
            )
            failed += 1

    print("-" * 60)
    print(
        f"1.2 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_check_permutation_tests()