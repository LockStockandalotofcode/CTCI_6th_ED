import itertools
import math

def get_permutations(s: str) -> list[str]:
    n = len(s)
    if n == 0: return [""] # this accounts to 1 permutation for 0!, for an empty string
    # otherwise there's no element for the loops to iterate on when creating the next permutation
    # if n == 1: return [s]

    # # recursive solution

    one_less_slice = slice(n-1)
    prev_perms = get_permutations(s[one_less_slice]) # of string with indices from 0 to n-2
    new_character = s[-1] # last character
    result = []
    for prev_perm in prev_perms:
        for i in range(n): # inserts the character at index-n in all permutations of first (n-1) characters
            new_perm = insert_char_at(prev_perm, new_character, i)
            result.append(new_perm)

    return result

def insert_char_at(string: str, char: str, pos: int) -> str:
    new_string = string[:pos] + char + string[pos:]
    return new_string

def run_permutations_tests():
    test_cases = [
        "",
        "a",
        "ab",
        "abc",
        "abcd",
        "pqrs",
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 8.7: PERMUTATIONS WITHOUT DUPS TESTS")
    print("=" * 60)

    for i, s in enumerate(test_cases, 1):
        try:
            res = get_permutations(s)

            # Standardize output for comparison
            if res is None:
                res = []

            # Expected combinations via python library
            expected_set = {"".join(p) for p in itertools.permutations(s)}
            expected_count = math.factorial(len(s))

            # 1. Cardinality check
            assert len(res) == expected_count, (
                f"For string '{s}', expected {expected_count} permutations,"
                f" got {len(res)}"
            )

            # 2. Duplicate generation check inside returned list
            assert len(res) == len(
                set(res)
            ), f"Returned list contains duplicate permutations: {res}"

            # 3. Content accuracy check
            assert (
                set(res) == expected_set
            ), f"Permutations set mismatch!\nExpected: {expected_set}\nGot: {set(res)}"

            print(
                f"  [PASS] Test {i:02d}: Input '{s}' -> {len(res)} Unique"
                " Permutations Validated"
            )
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: Input '{s}' -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"8.7 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_permutations_tests()