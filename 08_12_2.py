from typing import List
# EIGHT QUEENS

def place_queens(n: int = 8) -> List[List[int]]:
    """CTCI 8.12: Returns all valid board arrangements of N queens where result[i] = col of queen in row i."""
    # reecursion & backtracking solution
    return place_queens_helper(n, 0, [])

def place_queens_helper(n: int = 8, row: int = 0, curr_arrangement: list[int] = []) -> list[list[int]]:
    if row == n:
        return [curr_arrangement.copy()]

    solutions = []
    for col in range(n): # recursion 
        if check_valid_cell(col, row, curr_arrangement):
            curr_arrangement.append(col)
            # recurse
            # collect solutions from deeper cells along this path
            solutions.extend(place_queens_helper(n, row + 1, curr_arrangement))
            curr_arrangement.pop() # backtrack

    return solutions
    
def check_valid_cell(col: int, row: int, curr_arrangement: list[int]) -> bool:
    for row2, col2 in enumerate(curr_arrangement):
        # check for column clash
        if col == col2:
            return False
        # check for diagonal clash - difference between rows and cols is same for diagonal elements
        if abs(row - row2) == abs(col - col2):
            return False

    return True
    
def run_eight_queens_tests():
    def is_valid_solution(board: List[int], n: int) -> bool:
        if len(board) != n:
            return False
        cols, diag1, diag2 = set(), set(), set()
        for r, c in enumerate(board):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                return False
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)
        return True

    test_cases = [
        (1, 1, "1x1 board -> 1 valid solution"),
        (2, 0, "2x2 board -> 0 valid solutions"),
        (3, 0, "3x3 board -> 0 valid solutions"),
        (4, 2, "4x4 board -> 2 valid solutions"),
        (8, 92, "Standard 8x8 board -> 92 valid solutions"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 8.12: EIGHT QUEENS TESTS")
    print("=" * 60)

    for i, (n, expected_count, desc) in enumerate(test_cases, 1):
        try:
            solutions = place_queens(n)
            assert len(solutions) == expected_count, (
                f"Expected {expected_count} solutions for N={n}, got {len(solutions)}"
            )

            # Validate that every returned solution is non-attacking
            for sol in solutions:
                assert is_valid_solution(sol, n), f"Invalid non-attacking queen configuration: {sol}"

            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(f"8.12 SUMMARY: {passed} PASSED | {failed} FAILED | Total: {len(test_cases)}")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_eight_queens_tests()