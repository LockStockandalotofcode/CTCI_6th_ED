from typing import List, Tuple

def can_tile_with_dominos(
    rows: int, cols: int, removed_cells: List[Tuple[int, int]]
) -> bool:
    """CTCI 6.3: Returns True if board can be tiled with 1x2 dominoes."""
    # different color cells if removed in equal number, only then possible
    
    removed = [0, 0]
    for removed_cell in removed_cells:
        r = removed_cell[0]
        c = removed_cell[1]
        # cells with both indices even or odd, have one color (black for eg.)
        if (r % 2 == c % 2):
            removed[0] += 1
        # cells with one index even and another odd, have the second color (white for eg.)
        else:
            removed[1] += 1

    total_cells = (rows * cols)
    all_cells = [(total_cells - total_cells // 2), total_cells // 2] 
    all_cells[0] -= removed[0]
    all_cells[1] -= removed[1]

    if all_cells[0] != all_cells[1]:
        return False 
    return True


def run_dominos_tests():
    test_cases = [
        (
            8,
            8,
            [(0, 0), (7, 7)],
            False,
            "CTCI 8x8 with diagonally opposite corners cut (Same color)",
        ),
        (
            8,
            8,
            [(0, 0), (0, 1)],
            True,
            "8x8 with adjacent cells cut (Opposite colors removed)",
        ),
        (
            3,
            3,
            [(0, 0), (0, 1)],
            False,
            "Odd total remaining cells (7 remaining -> Impossible)",
        ),
        (2, 2, [], True, "2x2 board with 0 cutouts"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 6.3: DOMINOS TILING TESTS")
    print("=" * 60)

    for i, (r, c, cutouts, expected, desc) in enumerate(test_cases, 1):
        try:
            res = can_tile_with_dominos(r, c, cutouts)
            assert (
                res == expected
            ), f"Board {r}x{c} cutouts {cutouts}: Expected {expected}, got {res}"
            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"6.3 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__": 
    run_dominos_tests()