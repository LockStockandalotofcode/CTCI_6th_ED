import itertools
import math

def get_permutations(s: str) -> list[str]:
    n = len(s)
    if n == 0: return [""] # this accounts to 1 permutation for 0!, for an empty string
    # otherwise there's no element for the loops to iterate on when creating the next permutation
    # if n == 1: return [s]

    # # recursive solution 
    # building from permutations of all n-1 character substrings
    result = []
    for idx in range(n):
        string_before = s[:idx]
        string_after = s[idx + 1 : ]

        rest_perms = get_permutations(string_before + string_after)

        for rest in rest_perms:
            # can add the next character at either beginning or end, both work just fine
            result.append( rest + s[idx])
    
    return result

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