import collections
from typing import List, Union

def group_anagrams(strs: List[str]) -> Union[List[List[str]], List[str]]:
    if not strs: return strs
    # Hash table/ dict approach
    anagram_map = collections.defaultdict(list)
    # for i, string in enumerate(strs):
    for word in strs:
        key = "".join(sorted(word))
        anagram_map[key].append(word)

    return list(anagram_map.values())


def validate_grouped_anagrams(
    original: List[str], result: Union[List[List[str]], List[str]]
) -> bool:
    if result is None:
        return False

    # Normalize list of lists or flat list into groups
    if len(result) > 0 and isinstance(result[0], list):
        groups = result
    else:
        groups = []
        if result:
            curr_group = [result[0]]
            for word in result[1:]:
                if sorted(word) == sorted(curr_group[0]):
                    curr_group.append(word)
                else:
                    groups.append(curr_group)
                    curr_group = [word]
            groups.append(curr_group)

    # 1. Element preservation check
    flattened = [w for g in groups for w in g]
    if collections.Counter(flattened) != collections.Counter(original):
        return False

    # 2. Anagram group integrity
    for g in groups:
        first_sorted = sorted(g[0])
        if not all(sorted(w) == first_sorted for w in g):
            return False

    # 3. Maximum grouping check (No duplicate signature groups)
    group_signatures = [tuple(sorted(g[0])) for g in groups]
    if len(group_signatures) != len(set(group_signatures)):
        return False  # Anagrams were split across multiple groups!

    return True


def run_group_anagrams_tests():
    test_cases = [
        ([], "Empty input list"),
        (["a"], "Single element"),
        (["cat", "dog", "pig"], "No anagrams present"),
        (["eat", "tea", "tan", "ate", "nat", "bat"], "CTCI standard anagram set"),
        (["", "", "a", "a"], "Empty strings and duplicate single characters"),
        (["listen", "silent", "enlist", "google"], "Longer words with mixed group sizes"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 10.2: GROUP ANAGRAMS TESTS")
    print("=" * 60)

    for i, (strs, desc) in enumerate(test_cases, 1):
        try:
            res = group_anagrams(list(strs))
            assert validate_grouped_anagrams(
                strs, res
            ), f"Failed grouping validation for input {strs}. Got: {res}"

            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"10.2 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_group_anagrams_tests()