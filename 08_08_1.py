import itertools
import math

def get_permutations_with_dups(s: str) -> list[str]:
    n = len(s)
    if n == 0: return [""] # this accounts to 1 permutation for 0!, for an empty string
    # otherwise there's no element for the loops to iterate on when creating the next permutation
    # if n == 1: return [s]

    # # recursive solution

    one_less_slice = slice(n-1)
    prev_perms = get_permutations_with_dups(s[one_less_slice]) # of string with indices from 0 to n-2
    new_character = s[-1] # last character
    result = set()
    for i in range(n): # iterates from 0 until n-1, indicates position of inserting the new_character
        for prev_perm in prev_perms:
            new_perm = prev_perm[:i] + new_character + prev_perm[i:]
            result.add(new_perm)

    return list(result)

def run_permutations_with_dups_tests():
    # Format: (input_string, expected_unique_count, description)
    test_cases = [
        ("", 1, "Empty string"),
        ("a", 1, "Single character"),
        ("aaaa", 1, "All identical characters"),
        ("aab", 3, "Single duplicate character (3! / 2! = 3)"),
        ("aabb", 6, "Two duplicate pairs (4! / (2! * 2!) = 6)"),
        ("aabbc", 30, "Multiple duplicates (5! / (2! * 2!) = 30)"),
        ("abc", 6, "All unique characters (3! = 6)"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 8.8: PERMUTATIONS WITH DUPLICATES TESTS")
    print("=" * 60)

    for i, (s, expected_count, desc) in enumerate(test_cases, 1):
        try:
            res = get_permutations_with_dups(s)
            if res is None:
                res = []

            # Ground truth reference set
            expected_set = {"".join(p) for p in itertools.permutations(s)}

            # 1. Size check
            assert len(res) == expected_count, (
                f"Expected {expected_count} permutations for '{s}', got {len(res)}"
            )

            # 2. Duplicate generation check
            assert len(res) == len(set(res)), (
                f"Output contains duplicate permutations! Total: {len(res)}, Unique: {len(set(res))}"
            )

            # 3. Content accuracy
            assert set(res) == expected_set, (
                f"Generated set does not match ground truth.\nExpected: {expected_set}\nGot: {set(res)}"
            )

            print(f"  [PASS] Test {i:02d}: {desc} ('{s}' -> {len(res)} items)")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"8.8 SUMMARY: {passed} PASSED | {failed} FAILED | Total: {len(test_cases)}"
    )
    print("=" * 60 + "\n")
if __name__ == "__main__":
    run_permutations_with_dups_tests()