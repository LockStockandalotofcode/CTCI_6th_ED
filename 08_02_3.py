def get_path(matrix: list[list[int]]) -> list[int] | None:
    if not matrix or not matrix[0] or not matrix[0][0]: return None

    n_rows = len(matrix)
    n_cols = len(matrix[0])

    # bottom up approach- iterative solution, building the DP array
    # broken down into - step 1: record previous cell through which curremt cell is reachable
    # next step is done only in case destination is reachable at all
    # step 2: another traversal from destination to start point solely for tracking the path

    r, c = 0, 0
    dp = [[None] * n_cols for _ in range(n_rows)]
    # base case for 2D dp matrix
    dp[0][0] = (0, 0) # points to itself, indicating this is the start point 

    # in one while its not possible to fill the 2D dp array/ dp matrix
    # therefore, fill row by row

    # in this we only care about whther a node, a cell is reachable from the (0,0), thats also what we're storing in the 2D DP matrix
    for r in range(n_rows):
        for c in range(n_cols):
            # skip blocked cells and origin
            if not matrix[r][c] or (r == 0 and c == 0): continue

            # if previous top cell - is reachable
            # r > 0 and c > 0, is important since we do a check including r-1, and c-1 subsequently
            if r > 0 and dp[r - 1][c] is not None:
                dp[r][c] = (r-1, c)
            # if previous left cell - is reachable
            elif c > 0 and dp[r][c - 1] is not None:
                dp[r][c] = (r, c-1)
            
    if dp[n_rows - 1][n_cols - 1] is None: return None

    path = []
    curr = (n_rows - 1, n_cols - 1)
    while True:
        path.append(curr)
        if curr == (0,0): break
        curr_row = curr[0]
        curr_col = curr[1]
        curr = dp[curr_row][curr_col]

    path.reverse() # this method operates only on lists, mutates list in-place, thus avoids making copy and saves space/memory
    return path


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