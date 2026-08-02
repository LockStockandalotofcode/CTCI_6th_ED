def one_away(s1: str, s2: str) -> bool:
    if not s1 and not s2: return True

    # realisation for the strings to be one-away, they must not have a length difference of more than one
    if abs(len(s1) - len(s2)) > 1:
        return False
    
    if abs(len(s1) - len(s2)) == 0:
        # check for replacement
        replacement_count = 0
        for index_ptr in range(len(s1)):
            if s1[index_ptr] != s2[index_ptr]:
                replacement_count += 1
                if  replacement_count > 1:
                    return False
        return True

    if abs(len(s1) - len(s2)) == 1:
        # check for insertion or removal
        # choosing the longer string, reduces the problem to insertion (from smaller string's prespective) and removal from longer string's perspective

        longer = s1 if len(s1) > len(s2) else s2
        shorter = s1 if len(s1) < len(s2) else s2

        for index_ptr in range(len(shorter)):
            if shorter[index_ptr] != longer[index_ptr]:
                # first mismatch found 
                # if the rest of the characters are same, then return True, else there are more than 2 removals needed
                return shorter[index_ptr: ] == longer[index_ptr + 1: ]
                
        return True

def run_one_away_tests():
    test_cases = [
        # (s1, s2, expected)
        ("pale", "ple", True),  # Removal
        ("pales", "pale", True),  # Insertion
        ("pale", "bale", True),  # Replacement
        ("pale", "bake", False),  # 2 Replacements
        ("", "", True),  # Identical empty strings
        ("a", "", True),  # 1 Removal to empty
        ("a", "b", True),  # 1 Replacement
        ("a", "bc", False),  # Length diff > 1
        ("pas", "pale", False),  # 2 edits required
        ("pale", "pas", False),  # 2 edits required
    ]

    passed, failed = 0, 0
    print("\n" + "=" * 60)
    print("RUNNING CTCI 1.5: ONE AWAY TESTS")
    print("=" * 60)

    for i, (s1, s2, expected) in enumerate(test_cases, 1):
        try:
            res = one_away(s1, s2)
            assert res == expected, f"Expected {expected}, got {res}"
            print(f"  [PASS] Test {i:02d}: ('{s1}', '{s2}') -> {res}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: ('{s1}', '{s2}') -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"1.5 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_one_away_tests()