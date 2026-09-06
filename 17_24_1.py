import unittest

def _kadane_1d(arr: list[int]) -> tuple[int, int, int]:
    if not arr:
        return 0, 0, 0

    max_sum = float("-inf")
    current_sum = 0
    
    start = 0
    best_start = 0
    best_end = 0

    for i, val in enumerate(arr):
        current_sum += val
        if current_sum > max_sum:
            max_sum = current_sum
            best_start = start
            best_end = i

        if current_sum < 0:
            current_sum = 0
            start = i + 1

    return int(max_sum), best_start, best_end

def max_submatrix(matrix: list[list[int]]) -> int:
    # 2D kadane's 
    # time: O(R^2 + C)
    # space: O(C)

    if not matrix or not matrix[0]:
        return 0

    nr, nc = len(matrix), len(matrix[0])
    best_sum = float("-inf")
    best_bounds = (0, 0, 0, 0)# row_start, col_start, row_end, col_end

    for r_start in range(nr):
        col_sums = [0] * nc

        for r_end in range(r_start, nr):
            # accumulate column elements for row slice [r_start, r_end]
            for c in range(nc):
                col_sums[c] += matrix[r_end][c]

            # find best contiguous subarray in this subarray [r_start, r_end] and [column_x, column_y] determined by 1D kadane's algo
            current_max, c_start, c_end = _kadane_1d(col_sums)

            if current_max > best_sum:
                best_sum = current_max
                best_bounds = (r_start, c_start, r_end, c_end)

    return best_sum
            
# =====================================================================
# TEST SUITE
# =====================================================================
class TestMaxSubmatrix(unittest.TestCase):

    def test_01_empty_matrix(self):
        """Empty matrix returns sum 0."""
        self.assertEqual(max_submatrix([]), 0)

    def test_02_single_element_positive(self):
        """1x1 matrix with positive value."""
        self.assertEqual(max_submatrix([[5]]), 5)

    def test_03_all_negative_values(self):
        """Matrix with all negative values selects largest single element."""
        matrix = [[-5, -2], [-8, -3]]
        self.assertEqual(max_submatrix(matrix), -2)

    def test_04_all_positive_values(self):
        """Matrix with all positive values selects entire matrix."""
        matrix = [[1, 2], [3, 4]]
        self.assertEqual(max_submatrix(matrix), 10)

    def test_05_mixed_values_submatrix(self):
        """Finds maximal submatrix inside mixed positive and negative matrix."""
        matrix = [
            [1, -2, -1, 4],
            [-1, 3, 2, -2],
            [2, 0, -2, 1]
        ]
        self.assertEqual(max_submatrix(matrix), 5)


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.24 - Max Submatrix\n{'='*75}")

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
    run_tests(TestMaxSubmatrix)