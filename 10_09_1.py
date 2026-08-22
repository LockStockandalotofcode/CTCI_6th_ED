from typing import List, Tuple

def search_matrix(
    matrix: List[List[int]], target: int
) -> Tuple[int, int]:
    """CTCI 10.9: Finds target in row-and-column-sorted matrix (returns (-1, -1) if absent)."""
    # empty base case 
    if not matrix or not matrix[0]: return (-1, -1)

    n_rows = len(matrix)
    n_cols = len(matrix[0])

    # find row
    for r in range(n_rows):
        if matrix[r][0] <= target <= matrix[r][-1]:
            # binary search in particular row
            curr_row_check = search(matrix[r], 0, n_cols - 1, target)
            if curr_row_check != -1:
                return (r, curr_row_check)

    return (-1, -1)

def search(arr: list[int],left: int, right: int, target: int) -> int:
    if left > right:
        return -1
    # breakpoint()
    mid = left + (right - left) // 2
    
    if target == arr[mid]:
        return mid
    elif target < arr[mid]:
        # breakpoint()
        return search(arr, left, mid - 1, target)
    elif target > arr[mid]:
        return search(arr, mid + 1, right, target)

    return -1

def run_sorted_matrix_search_tests():
    mat = [
        [15, 20, 40, 85],
        [20, 35, 80, 95],
        [30, 55, 95, 105],
        [40, 80, 100, 120],
    ]

    test_cases = [
        ([], 55, (-1, -1), "Empty matrix input"),
        ([[]], 55, (-1, -1), "Matrix with empty row"),
        (mat, 55, (2, 1), "Target present in matrix (55 -> row 2, col 1)"),
        (mat, 15, (0, 0), "Target at top-left boundary"),
        (mat, 120, (3, 3), "Target at bottom-right boundary"),
        (mat, 10, (-1, -1), "Target smaller than minimum value"),
        (mat, 200, (-1, -1), "Target larger than maximum value"),
        (mat, 99, (-1, -1), "Target within range but absent"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 10.9: SORTED MATRIX SEARCH TESTS")
    print("=" * 60)

    for i, (matrix, target, expected_pos, desc) in enumerate(test_cases, 1):
        try:
            r, c = search_matrix(matrix, target)
            if expected_pos == (-1, -1):
                assert (
                    r == -1 and c == -1
                ), f"Expected (-1, -1) for target {target}, got ({r}, {c})"
            else:
                assert (
                    0 <= r < len(matrix)
                    and 0 <= c < len(matrix[0])
                    and matrix[r][c] == target
                ), (
                    f"Expected target {target} at valid matrix index, got"
                    f" ({r}, {c})"
                )
            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"10.9 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_sorted_matrix_search_tests()