from typing import List, Tuple

def search_matrix(
    matrix: List[List[int]], target: int
) -> Tuple[int, int]:
    """CTCI 10.9: Finds target in row-and-column-sorted matrix (returns (-1, -1) if absent)."""
    # empty base case 
    if not matrix or not matrix[0]: return (-1, -1)

    n_rows = len(matrix)
    n_cols = len(matrix[0])

    r, c = 0, n_cols - 1
    while 0 <= r < n_rows and 0 <= c < n_cols:
        if target < matrix[r][c]: # smaller than top element of column(minimum in this column)
            c -= 1
        elif target > matrix[r][c]: # bigger than rightmost element if this row(largest element of row)
            r += 1
        elif target == matrix[r][c]:
            return (r, c)

    return (-1, -1)

def _search_quadrant(matrix: list[list[int]], origin: tuple[int, int], dest: tuple[int, int], target: int) -> tuple[int, int]:
    start_r, start_c = origin
    end_r, end_c = dest

    # base case
    if start_r > end_r or start_c > end_c:
        return (-1, -1)
    if target < matrix[start_r][start_c] and target > matrix[end_r][end_c]:
        return (-1, -1)
    
    diag_length = min(end_r - start_r, end_c - start_c)
    low, high = 0, diag_length
    pivot_offset = 0

    # perform binary search on main diagonal to elimiate top-left and bottom-right quadrants
    while low <= high:
        mid = (low + high) // 2
        r, c = start_r + mid, start_c + mid 

        if target < matrix[r][c]:
            pivot_offset = mid
            low = mid + 1
        elif target > matrix[r][c]:
            high = mid - 1
        elif target == matrix[r][c]:
            return (r, c)

    # it gives the guide to go forward with sub quardants of the matrix
    pivot_r, pivot_c = pivot_offset + start_r, pivot_offset + start_c
    # recurse top-right quadrant
    top_right = _search_quadrant(matrix=matrix, 
                                 origin=(start_r, pivot_c + 1),
                                 dest=(pivot_r, end_c),
                                 target=target)
    if top_right != (-1, -1):
        return top_right
    # recurse bottom-left quadrant
    bottom_left = _search_quadrant(matrix=matrix, 
                                   origin=(pivot_r + 1, start_c),
                                   dest=(end_r, pivot_c),
                                   target=target)
    if bottom_left != (-1, -1):
        return bottom_left

    return (-1, -1)



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