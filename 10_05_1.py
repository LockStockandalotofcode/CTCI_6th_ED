def sparse_search(array: list[str], target: str) -> int:
    if not array or not target :
        return -1

    def binary_search_helper(left: int, right: int) -> int:
        if left > right:
            return -1
        
        mid = left + (right - left) // 2

        while mid > left and array[mid] == "":
            mid -= 1

        if array[mid] > target:
            return binary_search_helper(left, mid - 1)
        elif array[mid] < target:
            return binary_search_helper(mid + 1, right)
        elif array[mid] == target:
            return mid

        return -1

    return binary_search_helper(0, len(array) - 1)

def run_sparse_search_tests():
    test_cases = [
        ([], "ball", -1, "Empty array input"),
        (["", "", ""], "ball", -1, "Array containing only empty strings"),
        (["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], "", -1, "Target is empty string"),
        (["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], "ball", 4, "CTCI standard target lookup"),
        (["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], "at", 0, "Target at index 0"),
        (["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], "dad", 10, "Target near last element"),
        (["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""], "xyz", -1, "Non-existent target"),
        (["solo"], "solo", 0, "Single element match"),
    ]

    passed, failed = 0, 0
    print("\n" + "=" * 60)
    print("RUNNING CTCI 10.5: SPARSE SEARCH TESTS")
    print("=" * 60)

    for i, (arr, target, expected_idx, desc) in enumerate(test_cases, 1):
        try:
            res_idx = sparse_search(arr, target)
            if expected_idx == -1:
                assert res_idx == -1, f"Expected -1 for target '{target}', got index {res_idx}"
            else:
                assert res_idx != -1 and arr[res_idx] == target, (
                    f"Expected target '{target}' at index {expected_idx}, got index {res_idx}"
                )
            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(f"10.5 SUMMARY: {passed} PASSED | {failed} FAILED | Total: {len(test_cases)}")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_sparse_search_tests()