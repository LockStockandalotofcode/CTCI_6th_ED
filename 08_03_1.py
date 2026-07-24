# import pytest

def find_magic_index(arr: list[int]) -> int:
    # base case empty arr
    if not arr:
        return -1
    # early return optimisation
    size = len(arr)
    if arr[0] > size - 1:
        return -1
    if arr[-1] < 0:
        return -1

    for idx, num in enumerate(arr):
        if idx == num:
            return idx

    return -1



def run_magic_index_tests():
    test_cases = [
        # (arr, should_exist)
        # 1. Empty Case
        ([], False),
        # 2. Single Element Cases
        ([0], True),  # arr[0] == 0
        ([5], False),  # arr[0] != 0
        ([-1], False),
        # 3. Distinct Elements — Normal & Boundary Cases
        ([0, 2, 3, 4, 5], True),  # Magic at start (index 0)
        ([-10, -5, 2, 20, 30], True),  # Magic in middle (index 2)
        ([-10, -5, 0, 1, 4], True),  # Magic at end (index 4)
        ([1, 2, 3, 4, 5], False),  # No magic index (all A[i] > i)
        ([-10, -5, -1, 0], False),  # No magic index (all A[i] < i)
        # 4. Non-Distinct Elements / Duplicates (Subtle Edge Cases)
        ([-10, -5, 2, 2, 2, 5, 8], True),  # Duplicates: index 2 or 5 valid
        ([0, 1, 1, 1, 1, 1], True),  # Duplicates: index 0 or 1 valid
        ([-10, -10, -10, 1, 2, 3], False),  # Duplicates, no match
        ([1, 1, 1, 1, 1, 1], True),  # All identical, no match
        ([-10, -5, 1, 3, 3, 3, 3, 7, 9, 12, 13], True),  # Multiple clusters
    ]

    passed = 0
    failed = 0
    print("\n" + "=" * 60)
    print("RUNNING CTCI 8.3: MAGIC INDEX TESTS")
    print("=" * 60)

    for i, (arr, should_exist) in enumerate(test_cases, 1):
        try:
            result = find_magic_index(arr)

            if not should_exist:
                assert (
                    result == -1
                ), f"Expected -1 (no magic index), got {result}"
            else:
                assert (
                    result != -1
                ), f"Expected a valid magic index, got -1 on array {arr}"
                assert 0 <= result < len(arr), (
                    f"Index {result} is out of array bounds [0,"
                    f" {len(arr)-1}]"
                )
                assert arr[result] == result, (
                    f"Index {result} is invalid! arr[{result}] ="
                    f" {arr[result]} != {result}"
                )

            print(f"  [PASS] Test {i:02d}: arr = {arr}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: arr = {arr} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"8.3 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_magic_index_tests()