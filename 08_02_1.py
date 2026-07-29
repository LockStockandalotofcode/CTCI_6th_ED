def get_path(matrix: list[list[int]]) -> int:
    if not matrix or not matrix[0]: return 1

    n_rows = len(matrix)
    n_cols = len(matrix[0])

    path = []

    def helper( cell_r: int, cell_c: int) -> list[int, int] | None:
        # if cell is offlimit or the cell goes out of boundary of matrix
        if not matrix[cell_r][cell_c] or cell_r < 0 or cell_c < 0: return False

        # if either at start position, or a path exists to cell one above or a path exists to one cell to its left, we add this element, this procedure makes sure path that we get is from top-left to bottom-right destination
        if (cell_r == 0 and cell_c == 0) or helper(cell_r - 1, cell_c) or helper(cell_r, cell_c - 1):
            path.append((cell_r, cell_c))
            return True

        # this is equally crucial, if maybe path doesn't exist to this cell, then we must return something to backtrack
        return False

    # if path exists to the destination- bottom-right, then we return path. else, we return None
    if helper(n_rows - 1, n_cols - 1):
        return path
    return None

def run_robot_in_a_grid_tests():
    # True = Open, False = Obstacle
    grid_1 = [[True]]  # 1x1 Grid

    grid_open = [[True, True], [True, True]]  # 2x2 Open Grid

    grid_blocked_end = [[True, True], [True, False]]  # Destination Blocked

    grid_blocked_path = [
        [True, False, True],
        [True, False, True],
        [True, False, True],
    ]  # Wall cutting off grid

    grid_maze = [
        [True, True, False, True],
        [False, True, True, False],
        [True, False, True, True],
        [True, True, True, True],
    ]  # Winding valid path

    test_cases = [
        (grid_1, True),
        (grid_open, True),
        (grid_blocked_end, False),
        (grid_blocked_path, False),
        (grid_maze, True),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 8.2: ROBOT IN A GRID TESTS")
    print("=" * 60)

    for i, (grid, path_should_exist) in enumerate(test_cases, 1):
        R, C = len(grid), len(grid[0])
        try:
            path = get_path(grid)

            if not path_should_exist:
                assert (
                    not path
                ), f"Expected no path (None or []), but got path: {path}"
            else:
                assert (
                    path
                ), f"Expected a valid path, but got None or empty on grid {R}x{C}"
                assert (
                    path[0] == (0, 0)
                ), f"Path must start at (0, 0), got {path[0]}"
                assert path[-1] == (
                    R - 1,
                    C - 1,
                ), f"Path must end at ({R-1}, {C-1}), got {path[-1]}"

                # Validate step moves and obstacle collision
                for k in range(len(path)):
                    r, c = path[k]
                    assert (
                        0 <= r < R and 0 <= c < C
                    ), f"Path coordinate ({r}, {c}) out of bounds!"
                    assert grid[r][c], (
                        f"Path steps onto blocked obstacle at cell ({r}, {c})!"
                    )

                    if k > 0:
                        pr, pc = path[k - 1]
                        move = (r - pr, c - pc)
                        assert move in [(0, 1), (1, 0)], (
                            f"Invalid step from ({pr},{pc}) to ({r},{c}). Only"
                            " Right or Down allowed!"
                        )

            print(
                f"  [PASS] Test {i:02d}: Grid {R}x{C} (Path Expected:"
                f" {path_should_exist}) -> Valid"
            )
            passed += 1
        except Exception as e:
            print(
                f"  [FAIL] Test {i:02d}: Grid {R}x{C} (Path Expected:"
                f" {path_should_exist}) -> ERROR: {e}"
            )
            failed += 1

    print("-" * 60)
    print(
        f"8.2 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_robot_in_a_grid_tests()