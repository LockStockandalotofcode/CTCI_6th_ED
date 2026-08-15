def search_rotated(array: list[int], element) -> int:
    if not array or element is None:
        return -1

    def helper_search(left: int, right: int) -> int:
        if left > right: return -1
        mid = left + (right - left ) // 2 # standard lower mid calculation - works fine when not assigning left = mid, or right = mid
        # mid = left + (right - left + 1) // 2 # standard upper mid calculation - saves from infinite loops
        if array[mid] == element:
            return mid
        # one half is sorted, the other contains pivot
        if array[left] < array[mid]: # left half strictly sorted
            if array[left] <= element < array[mid]:
                return helper_search(left, mid - 1)
            else:
                return helper_search(mid + 1, right)
        elif array[mid] < array[right]:# right half striclty sorted
        # elif array[mid] < array[left]:# right half striclty sorted
            if array[mid] < element <= array[right]:
                return helper_search(mid + 1, right)
            else:
                return helper_search(left, mid - 1)
        else: # left and mid are equal
            # if rightmost is different, right must be sorted
            if array[left] != array[right]:
                return helper_search(mid + 1, right)
            # else ambiguous duplicates on both ends
            else:
                result = helper_search(left, mid - 1)
                if result == -1:
                    result = helper_search(mid + 1, right)
                return result

    return helper_search(0, len(array) - 1)

def run_search_rotated_tests():
    test_cases = [
        ([], 5, -1, "Empty array search"),
        ([10], 10, 0, "Single element match"),
        ([10], 5, -1, "Single element mismatch"),
        ([1, 2, 3, 4, 5], 3, 2, "Unrotated sorted array search"),
        (
            [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14],
            5,
            8,
            "CTCI standard rotated array",
        ),
        ([15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14], 25, 4, "Search pivot element"),
        (
            [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14],
            99,
            -1,
            "Target not present",
        ),
        (
            [2, 2, 2, 3, 4, 2, 2],
            3,
            3,
            "Rotated array with duplicate elements",
        ),
        (
            [2, 2, 2, 0, 2, 2],
            0,
            3,
            "Duplicates with target at pivot",
        ),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 10.3: SEARCH IN ROTATED ARRAY TESTS")
    print("=" * 60)

    for i, (arr, target, expected_idx, desc) in enumerate(test_cases, 1):
        try:
            res_idx = search_rotated(arr, target)

            if expected_idx == -1:
                assert (
                    res_idx == -1
                ), f"Expected -1 for missing target {target}, got {res_idx}"
            else:
                assert res_idx != -1 and arr[res_idx] == target, (
                    f"Expected index with value {target}, got index {res_idx}"
                    f" (val={arr[res_idx] if 0 <= res_idx < len(arr) else 'OUT_OF_BOUNDS'})"
                )

            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"10.3 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")
if __name__ == "__main__":
    run_search_rotated_tests()