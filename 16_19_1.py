import unittest

def pond_sizes(land: list[list[int]]) -> list[int]:
    if not land or not land[0]:
        return []

    n_rows = len(land)
    n_cols = len(land[0])
    visited = set()
    results = []

    
    # dfs on all 0 cells, tracking all visited cells
    def helper(row: int, col: int) -> int:
        if row >= n_rows or row < 0:
            return 0
        if col >= n_cols or col < 0:
            return 0
        if land[row][col] != 0 or (row, col) in visited:
            return 0

        visited.add((row, col))
        size = 1

        neighbors = [
            [-1, 0],  # Up
            [-1, 1],  # Up-Right
            [0, 1],   # Right
            [1, 1],   # Down-Right
            [1, 0],   # Down
            [1, -1],  # Down-Left
            [0, -1],  # Left
            [-1, -1]  # Up-Left
        ]

        for neighbor in neighbors:
            offset_row = neighbor[0]
            offset_col = neighbor[1]

            next_row = row + offset_row
            next_col = col + offset_col

            size += helper(next_row, next_col)

        return size

    for r in range(n_rows):
        for c in range(n_cols):
            if land[r][c] == 0 and (r, c) not in visited:
                results.append(helper(r, c))

    return sorted(results)



# # =====================================================================
# # SOLUTION PLACEHOLDER
# # Replace or import your actual function here
# # =====================================================================
# def pond_sizes(land: list[list[int]]) -> list[int]:
#     """Computes all pond sizes in a grid where 0 indicates water.
#     Includes all 8 horizontal, vertical, and diagonal directions.
#     """
#     if not land or not land[0]:
#         return []

#     rows, cols = len(land), len(land[0])
#     visited = set()
#     sizes = []

#     def compute_size(r, c):
#         if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or land[r][c] != 0:
#             return 0
#         visited.add((r, c))
#         size = 1
#         for dr in (-1, 0, 1):
#             for dc in (-1, 0, 1):
#                 if dr != 0 or dc != 0:
#                     size += compute_size(r + dr, c + dc)
#         return size

#     for r in range(rows):
#         for c in range(cols):
#             if land[r][c] == 0 and (r, c) not in visited:
#                 sizes.append(compute_size(r, c))

#     return sorted(sizes)


# =====================================================================
# TEST SUITE
# =====================================================================
class TestPondSizes(unittest.TestCase):

    def test_01_empty_grid(self):
        """Empty grid returns empty list."""
        self.assertEqual(pond_sizes([]), [])
        self.assertEqual(pond_sizes([[]]), [])

    def test_02_all_land(self):
        """Grid with no water (all non-zero values) returns empty list."""
        grid = [[1, 2], [3, 4]]
        self.assertEqual(pond_sizes(grid), [])

    def test_03_all_water(self):
        """Grid with all zeros forms a single large pond."""
        grid = [
            [0, 0],
            [0, 0]
        ]
        self.assertEqual(pond_sizes(grid), [4])

    def test_04_diagonal_connectivity(self):
        """Water tiles connected diagonally form a single pond."""
        grid = [
            [0, 1],
            [1, 0]
        ]
        self.assertEqual(pond_sizes(grid), [2])

    def test_05_ctci_example(self):
        """Standard CTCI example grid returning multiple pond sizes [2, 4, 1]."""
        grid = [
            [0, 2, 1, 0],
            [0, 1, 0, 1],
            [1, 1, 0, 1],
            [0, 1, 0, 1]
        ]
        self.assertEqual(pond_sizes(grid), [1, 2, 4])

    def test_06_single_element_water(self):
        """Single 1x1 grid containing water."""
        self.assertEqual(pond_sizes([[0]]), [1])

    def test_07_multiple_isolated_ponds(self):
        """Isolated single-cell water spots."""
        grid = [
            [0, 5, 0],
            [5, 5, 5],
            [0, 5, 0]
        ]
        self.assertEqual(pond_sizes(grid), [1, 1, 1, 1])


# =====================================================================
# INFORMATIVE TEST RUNNER
# =====================================================================
def run_informative_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.19 - Pond Sizes\n{'='*75}")

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
    print(f" EXECUTION SUMMARY:")
    print(f" Total Tests : {total}")
    print(f" Passed      : {passed} ✅")
    print(f" Failed      : {failed} ❌")
    print(f" Errors      : {errors} ⚠️")
    print(f" Success Rate: {pass_rate:.1f}%")
    print(f"{'='*75}\n")


if __name__ == "__main__":
    run_informative_tests(TestPondSizes)