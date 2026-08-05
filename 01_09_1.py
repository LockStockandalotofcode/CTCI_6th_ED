"""
s1:
waterbottle

s2:
erbottlewat

# Brute-Force
check if longer subpart - (here erbottle) isSubstring(s1)
followed by single character checking of the rest of characters

whenever condition not met -> gives strings are not rotation

String Rotation is basically: s1 = xy, s2 = yx
if we concatenate s2 + s2: yxyx, then s1 isSubstring of s2+s2
if s1 is not Substring of s2+s2, then they are not string rotations

"""

def is_substring(sub: str, main: str) -> bool:
    return sub in main

def is_string_rotation(s1:str, s2:str) -> bool:
    if not s1 and not s2:
        return True
    if not s1 or not s2: 
        return False

    if len(s1) != len(s2):
        return False

    concatenated_str = s2 + s2
    if is_substring(s1, concatenated_str):
        return True
    else:
        return False

def run_string_rotation_tests():
    test_cases = [
        # (s1, s2, expected)
        ("", "", True),
        ("a", "", False),
        ("", "a", False),
        ("a", "a", True),
        ("a", "b", False),
        ("ab", "ba", True),
        ("ab", "ab", True),
        ("waterbottle", "erbottlewat", True),
        ("waterbottle", "erbotlewatt", False),  # Typo/length trick
        ("aaata", "aataa", True),  # Repeated character traps
        ("abab", "baba", True),
        ("abcd", "acbd", False),  # Permutation but not rotation
        ("a" * 1000 + "b", "b" + "a" * 1000, True),  # Scaled rotation
        ("hello", "helloo", False),  # Unequal lengths
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 1.9: STRING ROTATION TESTS")
    print("=" * 60)

    for i, (s1, s2, expected) in enumerate(test_cases, 1):
        try:
            res = is_string_rotation(s1, s2)
            assert (
                res == expected
            ), f"s1='{s1}', s2='{s2}' | Expected {expected}, got {res}"
            print(
                f"  [PASS] Test {i:02d}: ('{s1[:10]}...', '{s2[:10]}...') ->"
                f" {res}"
            )
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: ('{s1}', '{s2}') -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"1.9 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_string_rotation_tests()
        