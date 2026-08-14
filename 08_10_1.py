from typing import List

def paint_fill(screen: List[List[int]], r: int, c: int, new_color: int) -> List[List[int]]:
    if not 0 <= r < len(screen) or not 0 <= c < len(screen[0]):
        return screen
    # we need to color all connected cells (contiguous by original color) the same as new-color
    if new_color == screen[r][c]:
        return screen
    if not screen:
        return screen
    return recursive_helper(screen, r, c, screen[r][c], new_color)
    
def recursive_helper(screen: list[list[int]], r: int, c: int, org_color: int, new_color: int) -> list[list[int]]:
    screen[r][c] = new_color
    neighbors = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    for neighbor in neighbors:
        neighbor_row = r + neighbor[0]
        neighbor_col = c + neighbor[1]
        if not 0 <= neighbor_row < len(screen) or not 0 <= neighbor_col < len(screen[0]):
            continue

        neighbor_cell_color = screen[neighbor_row][neighbor_col]
        if neighbor_cell_color == org_color:
            recursive_helper(screen, neighbor_row, neighbor_col, org_color, new_color)

    return screen

def run_paint_fill_tests():
    test_cases = [
        (
            [
                [1, 1, 1],
                [1, 1, 0],
                [1, 0, 1],
            ],
            1,
            1,
            2,
            [
                [2, 2, 2],
                [2, 2, 0],
                [2, 0, 1],
            ],
            "Standard connected component fill",
        ),
        (
            [[1, 1], [1, 1]],
            0,
            0,
            1,
            [[1, 1], [1, 1]],
            "No-op fill (new_color == target_color)",
        ),
        (
            [[5]],
            0,
            0,
            9,
            [[9]],
            "Single cell grid fill",
        ),
        (
            [[1, 2], [3, 4]],
            -1,
            0,
            9,
            [[1, 2], [3, 4]],
            "Out of bounds negative row coordinate",
        ),
        (
            [[1, 2], [3, 4]],
            0,
            5,
            9,
            [[1, 2], [3, 4]],
            "Out of bounds column coordinate",
        ),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 8.10: PAINT FILL TESTS")
    print("=" * 60)

    for i, (grid, r, c, new_color, expected, desc) in enumerate(test_cases, 1):
        grid_copy = [list(row) for row in grid]
        try:
            res = paint_fill(grid_copy, r, c, new_color)
            if res is None:
                res = grid_copy  # Handle in-place mutation without return

            assert (
                res == expected
            ), f"Expected grid:\n{expected}\nGot grid:\n{res}"
            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"8.10 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_paint_fill_tests()