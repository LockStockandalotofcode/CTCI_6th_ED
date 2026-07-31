import copy
def rotate_matrix(matrix: list[list]) -> list[list]:
    if not matrix or not matrix[0]: return []

    n = len(matrix) # size of matrix
    # in-place algorithm
    # 90-degree rotation boils down to swapping the 4-edges of a square matrix, top->left->bottom->right->top, 
    # starting at the outer layer, until we reach the centre

    # for odd-size square matrix, its always (size - 1)/2 layers until centre
    # for even-size square matrix, its always (size)/2 layers until centre
    layers = n // 2
    # swapping 4 layers/arrays is simply done by storing the first value as temp, and follows
    for layer in range(layers):
        first = layer
        last = (n-1) - first
        for i in range(first, last): # i stops at 1 before last, because we include only one corner per single side(top, right, bottom, left)
            offset = i - first  # gives how long we've come from the corner of a side

            # Now we swap the 4 elements in a circle one-by-one
            # save the element in top row temporarily
            top = matrix[first][i]

            # from left edge to top edge
            matrix[first][i] = matrix[last - offset][first]
            # from bottom edge to lefft edge
            matrix[last - offset][first] = matrix[last][last - offset]
            # from right edge to bottom edge
            matrix[last][last - offset] = matrix[i][last]

            # crucial: put the earlier temporarily saved  
            # from top edge to right edge
            matrix[i][last] = top

            # The rule for in-place swapping(not the dynamic swapping allowed by python) : "Fill the empty spot"
            # if we save top in a temporary variable first, top becomes our empty spot, 
            # and we work backwards to fill empty spots, so that we never overwrite an unread value
    
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