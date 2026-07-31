import copy
def rotate_matrix(matrix: list[list]) -> list[list]:
    if not matrix or not matrix[0]: return []

    n = len(matrix) # size of matrix
    # easy way: take transpose of matrix/image across the main diagonal(from top-left to bottom-right diagonal), and then mirror image along y-axix/vertically
    # plus point this can be done in-place: O(1) space complexity

    # step 1 - Transpose
    
    # row-wise traversal
    # swapping only non-diagonal(except for diagonal from top-left to bottom-right) diagonal, with their symmetric element across this diagonal
    # row-wise traversal, column traversal for each row, starts from c = r + 1 until n
    # we go through all elements of the upper diagonal, and then swap them with the element intended
    for r in range(n):
        for c in range(r+1, n):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    # Step 2 - vertical mirror image/ image across y axis
    for r in range(n): # works for both even and odd size matrix
        for c in range(n // 2):
            matrix[r][c], matrix[r][(n-1) - c] = matrix[r][(n-1) - c], matrix[r][c]

    return matrix

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