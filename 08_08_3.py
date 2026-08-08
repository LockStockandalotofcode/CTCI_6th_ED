import itertools
# (this does not create all permmutations and remove the duplicates like method 1 (highly inefficient for high character frequency strings)

def get_permutations_with_dups(s: str) -> list[str]:
    # recursive solution
    # build hash-map of character-frequency in a dict
    # picking one prefix character, we have a subproblem
    # which boils down to subproblem with 0 chracter --> base case, returning ""
    hash_table = {}
    for char in s:
        hash_table[char] = hash_table.get(char, 0) + 1
    result = []
    def backtrack(prefix: str, remaining_length: int):
        if remaining_length == 0:
            result.append(prefix)
            return

        for char, freq in hash_table.items():
            if freq > 0:
                # choose a character as the current prefix
                # decrement its frequency in the hash table, to skip this in recursion step
                hash_table[char] -= 1
                # build permutation of rest of the string
                backtrack(prefix + char, remaining_length - 1)
                # add the character, BACKTRACK
                hash_table[char] += 1

    backtrack("", len(s))
    return result

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