# edit = insert, remove, replace

def insert_char(s: list, new_char: str, index: int) -> str:
    prefix_slice = slice(index)
    suffix_slice = slice(index, len(s))
    result = s[prefix_slice] + list(new_char) + s[suffix_slice]
    return "".join(result)

def replace_char(s: list, new_char: str, index: int) -> str:
    prefix_slice = slice(index)
    suffix_slice = slice(index + 1, len(s))
    result = s[prefix_slice] + list(new_char) + s[suffix_slice]
    return "".join(result)

def remove(s: list, index: int) -> str:
    prefix_slice = slice(index)
    suffix_slice = slice(index + 1, len(s) )
    result = s[prefix_slice] + s[suffix_slice]
    return "".join(result)

def one_away(s1: str, s2: str) -> bool:
    if not s1 and not s2: return True

    # to ensure s1 is the shorter string and s2 is the longer
    if len(s1) > len(s2):
        s1, s2 = s2, s1
        list_s1 = list(s2)
    list_s1 = list(s1)

    # looping through the longer string
    for idx, char in enumerate(s2):
        removed_char_s1 = remove(list_s1, idx)
        if removed_char_s1 == s2:
            return True

        for i in range(97, 123):
            new_char = chr(i)
            inserted_new_char_s1 = insert_char(list_s1, new_char, idx)
            if inserted_new_char_s1 == s2: 
                return True
            replaced_new_char_s1 = replace_char(list_s1, new_char, idx)
            if replaced_new_char_s1 == s2: 
                return True

    return False

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