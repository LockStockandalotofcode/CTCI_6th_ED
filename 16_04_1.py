import unittest
from typing import Optional, List

# for repetitive or frequent lookups, on 3 x 3 board, use state hash map
# map 3x3 string grid to base-3 integer key
# generate all 3^9 possible boards, decode to board, and hash the values in a dict

def _check_line(board: List[List[str]], row_start: int, col_start: int, row_step: int, col_step: int) -> Optional[str]:
    n = len(board)
    first_char = board[row_start][col_start]

    if first_char == " " or "":
        return ""

    r, c = row_start + row_step, col_start + col_step
    for _ in range(1, n):
        if board[r][c] != first_char:
            return ""
        r += row_step
        c += col_step

    return first_char

def tic_tac_win(board: list[list[str]]) -> Optional[str]:
    # General solutions for N x N board
    #  time complexity O(N), auxiliary space: O(1)

    if not board or not board[0]:
        return ""

    n = len(board)

    # check all rows, and columns
    for i in range(n):
        # row i
        row_winner = _check_line(board, row_start=i, col_start=0, row_step=0, col_step=1)
        if row_winner:
            return row_winner

        # column i
        col_winner = _check_line(board, row_start=0, col_start=i, row_step=1, col_step=0)
        if col_winner:
            return col_winner

    # check main diagonal, anti-diagonal
    diag_1_winner = _check_line(board, row_start=0, col_start=0, row_step=1, col_step=1)
    if diag_1_winner:
        return diag_1_winner
    diag_2_winner = _check_line(board, row_start=0, col_start=len(board[0]) - 1, row_step=1, col_step=-1)
    if diag_2_winner:
        return diag_2_winner

    return ""

# =====================================================================
# TEST SUITE
# =====================================================================
class TestTicTacWin(unittest.TestCase):

    def test_01_empty_board(self):
        """Empty board returns no winner."""
        self.assertEqual(tic_tac_win([]), "")

    def test_02_row_win_x(self):
        """Winning condition along a horizontal row for 'X'."""
        board = [
            ["X", "X", "X"],
            ["O", "O", ""],
            ["", "", ""]
        ]
        self.assertEqual(tic_tac_win(board), "X")

    def test_03_column_win_o(self):
        """Winning condition along a vertical column for 'O'."""
        board = [
            ["O", "X", ""],
            ["O", "X", ""],
            ["O", "", "X"]
        ]
        self.assertEqual(tic_tac_win(board), "O")

    def test_04_main_diagonal_win(self):
        """Winning condition along the main diagonal (top-left to bottom-right)."""
        board = [
            ["X", "O", ""],
            ["O", "X", ""],
            ["", "", "X"]
        ]
        self.assertEqual(tic_tac_win(board), "X")

    def test_05_anti_diagonal_win(self):
        """Winning condition along the anti-diagonal (top-right to bottom-left)."""
        board = [
            ["X", "", "O"],
            ["X", "O", ""],
            ["O", "", "X"]
        ]
        self.assertEqual(tic_tac_win(board), "O")

    def test_06_nxn_board_generic(self):
        """Works for arbitrary N x N boards (4x4 board)."""
        board = [
            ["O", "X", "X", "X"],
            ["O", "O", "X", ""],
            ["X", "", "O", ""],
            ["", "", "", "O"]
        ]
        self.assertEqual(tic_tac_win(board), "O")

    def test_07_ongoing_game_no_winner(self):
        """Incomplete game with no winner returns empty string."""
        board = [
            ["X", "O", "X"],
            ["X", "O", ""],
            ["O", "X", ""]
        ]
        self.assertEqual(tic_tac_win(board), "")


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.4 - Tic Tac Win\n{'='*75}")

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
            print(f"  ❌ [FAIL] {desc}")
            failed += 1
        elif result.errors:
            print(f"  ⚠️  [ERROR] {desc}")
            errors += 1

    total = passed + failed + errors
    pass_rate = (passed / total * 100) if total > 0 else 0.0

    print(f"\n{'-'*75}")
    print(f" SUMMARY: Total: {total} | Passed: {passed} ✅ | Failed: {failed} ❌ | Errors: {errors} ⚠️ | Rate: {pass_rate:.1f}%")
    print(f"{'='*75}\n")


if __name__ == "__main__":
    run_tests(TestTicTacWin)