import unittest
from typing import Optional

class SquareCell:
    # helper class storing counts of contiguous black cells to the right and below
    def __init__(self, right: int = 0, below: int = 0):
        self.right = right
        self.below = below

def _precompute_black_borders(matrix: list[list[int]]) -> list[list[SquareCell]]:
    # helper precomputes consecutive black cells to. the right and bottom
    # time: O(N ^ 2)
    n = len(matrix)
    grid = [[SquareCell() for _ in range(n)] for _ in range(n)]

    for r in range(n-1, -1, -1):
        for c in range(n-1, -1, -1):
            if matrix[r][c] == 0: # representing black cells
                right_cnt = 1 + (grid[r][c + 1].right if c + 1 < n else 0)
                below_cnt = 1 + (grid[r + 1][c].below if r + 1 < n else 0)
                grid[r][c] = SquareCell(right_cnt, below_cnt)

    return grid

def _validate_square(grid: list[list[SquareCell]], r: int, c: int, size: int) -> bool:
    # helper validates if all 4 borders of candidate squareare black in O(1) time
    top_left = grid[r][c]
    bottom_left = grid[r + size - 1][c]
    top_right = grid[r][c + size - 1]

    # Verify all 4 pointers have at least 'size' black cells:        
    if top_left.right < size or top_left.below < size:
        return False
    if bottom_left.right < size:
        return False
    if top_right.below < size:
        return False

    return True

def find_max_black_square(matrix: list[list[int]]) -> tuple[int, int, int] | None:
    # DP, constructing Lookup Grid
    # returns (row, col, size) of maximum black square or None
    # Time: O(N ^ 3)
    # SpacE: O(N ^ 2)
    if not matrix or not matrix[0]:
        return None

    n = len(matrix)
    grid = _precompute_black_borders(matrix)

    # check starting from largest possible square first
    for size in range(n, 0, -1):
        for r in range(n - size + 1):
            for c in range(n - size + 1):
                if _validate_square(grid, r, c, size):
                    return (r, c, size)

    return None


# =====================================================================
# TEST SUITE
# =====================================================================
class TestMaxBlackSquare(unittest.TestCase):

    def test_01_empty_matrix(self):
        """Empty matrix returns None."""
        self.assertEqual(find_max_black_square([]), None)

    def test_02_all_white_pixels(self):
        """Matrix with only white pixels (1s) returns None."""
        matrix = [[1, 1], [1, 1]]
        self.assertEqual(find_max_black_square(matrix), None)

    def test_03_single_black_pixel(self):
        """Single black pixel forms a 1x1 subsquare."""
        matrix = [
            [1, 1],
            [1, 0]
        ]
        self.assertEqual(find_max_black_square(matrix), (1, 1, 1))

    def test_04_full_black_matrix(self):
        """Entire grid filled with black pixels returns full matrix dimensions."""
        matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(find_max_black_square(matrix), (0, 0, 3))

    def test_05_hollow_black_border_with_white_interior(self):
        """Square with black borders and white interior is valid."""
        matrix = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        self.assertEqual(find_max_black_square(matrix), (0, 0, 3))


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.23 - Max Black Square\n{'='*75}")

    passed, failed, errors = 0, 0, 0

    for test in suite:
        test_name = test._testMethodName
        doc = (test._testMethodDoc or "").strip()
        desc = f"{test_name} -> {doc}" if doc else test_name

        result = unittest.TestResult()
        test.run(result)

        if result.wasSuccessful():
            print(f"  ✅ [PASS] {desc}")
            passed += 1
        elif result.failures:
            fail_msg = result.failures[0][1].strip().split("\n")[-1]
            print(f"  ❌ [FAIL] {desc} | {fail_msg}")
            failed += 1
        elif result.errors:
            err_msg = result.errors[0][1].strip().split("\n")[-1]
            print(f"  ⚠️  [ERROR] {desc} | {err_msg}")
            errors += 1

    total = passed + failed + errors
    pass_rate = (passed / total * 100) if total > 0 else 0.0

    print(f"\n{'-'*75}")
    print(
        f" SUMMARY: Total: {total} | Passed: {passed} ✅ | Failed: {failed} ❌ | Errors: {errors} ⚠️ | Rate: {pass_rate:.1f}%"
    )
    print(f"{'='*75}\n")


if __name__ == "__main__":
    run_tests(TestMaxBlackSquare)