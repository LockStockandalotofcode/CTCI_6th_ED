import copy

def zero_matrix(matrix: list[list[int]]) -> list[list[int]]:
    if not matrix or not matrix[0]: return matrix
    rows = len(matrix)
    cols = len(matrix[0])

    first_row_flag = any(matrix[0][c] == 0 for c in range(cols))
    first_col_flag = any(matrix[r][0] == 0 for r in range(rows))

    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                matrix[r][0] = 0
    # detection done

    # now in place mutation of matrix
    # do the work on all cells spanning from row 1 to end, col 1 to end
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][0] == 0 or matrix[0][c] == 0:
                matrix[r][c] = 0

    # fixing first row
    if first_row_flag:
        for c in range(cols):
            matrix[0][c] = 0
    # fixing first column
    if first_col_flag:
        for r in range(rows):
            matrix[r][0] = 0

    return matrix

def run_zero_matrix_tests():
    test_cases = [
        ([], []),
        ([[0]], [[0]]),
        ([[1]], [[1]]),
        ([[1, 0, 1], [1, 1, 1], [1, 1, 1]], [[0, 0, 0], [1, 0, 1], [1, 0, 1]]),
        (
            [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
            [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
        ),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 1.8: ZERO MATRIX TESTS")
    print("=" * 60)

    for i, (initial, expected) in enumerate(test_cases, 1):
        m = copy.deepcopy(initial)
        try:
            res = zero_matrix(m)
            actual = m if res is None else res
            assert actual == expected, f"\nExpected:\n{expected}\nGot:\n{actual}"
            print(
                f"  [PASS] Test {i:02d}: Matrix"
                f" {len(initial)}x{len(initial[0]) if initial else 0} Processed"
            )
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"1.8 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_zero_matrix_tests()