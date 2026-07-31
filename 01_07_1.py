def rotate_matrix(matrix: list[list]) -> list[list]:
    if not matrix or not matrix[0]: return []

    n_rows = len(matrix)
    n_cols = len(matrix[0])
    rotated_matrix = [[0 for _ in range(n_cols)] for _ in range(n_rows)]

    # a row at index r, becomes a column at index c = (no_of_rows - 1) - r
    # converting one row at a time, starting at bottom-most row, as that becomes the first column, for simpler addition
    for r in reversed(range(n_rows)): # for n_rows = 5, this iterates over 4, 3, 2, 1, 0
        curr_row = matrix[r]
        col_idx = (n_rows - 1) - r
        for idx in range(n_rows):
            row_idx = idx
            rotated_matrix[row_idx][col_idx] = curr_row[idx]

    return rotated_matrix

import copy


def run_rotate_matrix_tests():
    test_cases = [
        # Empty and 1x1
        ([], []),
        ([[1]], [[1]]),
        # 2x2
        ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
        # 3x3
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[7, 4, 1], [8, 5, 2], [9, 6, 3]],
        ),
        # 4x4
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16],
            ],
            [
                [13, 9, 5, 1],
                [14, 10, 6, 2],
                [15, 11, 7, 3],
                [16, 12, 8, 4],
            ],
        ),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 1.7: ROTATE MATRIX TESTS")
    print("=" * 60)

    for i, (initial, expected) in enumerate(test_cases, 1):
        m = copy.deepcopy(initial)
        try:
            res = rotate_matrix(m)
            # Accept either in-place modification of m OR returning mutated res
            actual = m if res is None else res
            assert actual == expected, f"\nExpected:\n{expected}\nGot:\n{actual}"
            print(f"  [PASS] Test {i:02d}: {len(initial)}x{len(initial)} Rotated")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"1.7 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_rotate_matrix_tests()