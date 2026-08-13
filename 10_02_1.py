import collections
from typing import List, Union

def group_anagrams(strs: List[str]) -> Union[List[List[str]], List[str]]:
    if not strs: return strs
    # 2-pointer approach
    final_result = []
    visited = set()
    # while i < len(strs) and i < j and j < len(strs):
    for i, str1 in enumerate(strs):
        result = []
        if str1 in visited:
            continue
        result.append(str1)
        visited.add(str1)
        for j in range(i+1, len(strs)):
            # if anagram: add the anagram to the set
            # for all elements who have appended to result list, this calls checkanagrams fn repeatedly, but using visited for this, would also skip the duplicate elements in original strs array
            if check_anagrams(strs[i], strs[j]):
                result.append(strs[j])
                visited.add(strs[j])
            # else continue looping

        # once one string's anagrams are covered, add them to te=he final result
        final_result.append(result)

    return final_result

def check_anagrams(str1: str, str2: str) -> bool:
    if len(str1) != len(str2):
        return False
    if sort_string(str1) == sort_string(str2):
        return True
    else:
        return False

def sort_string(string: str) -> str:
    string = sorted(string)
    return "".join(string)


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