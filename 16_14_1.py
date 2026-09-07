import unittest
import math
from collections import defaultdict

class Point:
    # a 2D point
    def __init__(self, x: float, y: float):
        self.x = float(x)
        self.y = float(y)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Point):
            return False
        return abs(self.x - other.x) < 0.0001 and abs(self.y - other.y) < 0.0001

    def __hash__(self) -> int:
        # hash the tuple
        # custom hashning erquired when equality is customised
        return hash(( round(self.x, 4), round(self.y, 4) ))

class Line: 
    EPSILON = 0.0001
    def __init__(self, p1: Point, p2: Point):
        if abs(p1.x - p2.x) < Line.EPSILON:
            # Vertical line, slope is infinity, intercept is x-intercept
            self.slope = float("inf")
            self.intercept = round(p1.x, 4)
        else:
            slope = ((p2.y - p1.y) / (p2.x - p1.x))
            self.slope = 0.0 if abs(slope) < Line.EPSILON else round(slope, 4)

            intercept = (p1.y - self.slope * p1.x)
            self.intercept = (
                0.0 if abs(intercept) < Line.EPSILON else round(intercept, 4)
            )

    # def _floor_to_epsilon(self, val:float) -> float:
    #     # helper round values to epsilon tolerance to prevetn floating key mismatch
    #     r = int(val / Line.EPSILON)
    #     return float(r) * Line.EPSILON

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Line):
            return False
        return (
            abs(self.slope - other.slope) < Line.EPSILON 
            and abs(self.intercept - other.intercept) < Line.EPSILON 
        )

    def __hash__(self) -> int:
        return hash((self.slope, self.intercept))

    def to_tuple(self) -> tuple[float | None, float]:
        if self.slope == float("inf"):
            return (None, self.intercept)
        return (self.slope, self.intercept)

def find_best_line(points: list[tuple[float, float]]) -> tuple[float, float] | tuple[float | None, float]:
    # Pairwise Line Hashing
    # time: O(N ^ 2)
    # Space: O(N ^ 2)
    
    if not points:
        return (0.0, 0.0)

    pts = [p if isinstance(p, Point) else Point(p[0], p[1]) for p in points]

    if len(pts) < 2:
        return (None, pts[0].x)
        # i.e. the vertical line through point[0], the only point

    lines_map: dict[Line, int] = {}
    best_line = None
    max_points = 0

    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            line = Line(pts[i], pts[j])

            lines_map[line] = lines_map.get(line, 0) + 1

            if lines_map[line] > max_points:
                max_points = lines_map[line]
                best_line = line

    return best_line.to_tuple() if best_line else (None, pts[0].x)


# =====================================================================
# TEST SUITE
# =====================================================================
class TestBestLine(unittest.TestCase):

    def test_01_empty_and_single_point(self):
        """Single point returns default line passing through the point."""
        self.assertEqual(find_best_line([(2.0, 3.0)]), (None, 2.0))

    def test_02_vertical_line_points(self):
        """Identifies vertical line with infinite slope correctly."""
        points = [(1.0, 2.0), (1.0, 5.0), (1.0, -3.0), (2.0, 4.0)]
        self.assertEqual(find_best_line(points), (None, 1.0))

    def test_03_horizontal_line_points(self):
        """Identifies horizontal line with zero slope correctly."""
        points = [(1.0, 4.0), (3.0, 4.0), (-2.0, 4.0), (0.0, 1.0)]
        self.assertEqual(find_best_line(points), (0.0, 4.0))

    def test_04_diagonal_line_points(self):
        """Finds diagonal line y = 2x + 1 through maximum collinear points."""
        points = [(0.0, 1.0), (1.0, 3.0), (2.0, 5.0), (3.0, 10.0)]
        self.assertEqual(find_best_line(points), (2.0, 1.0))

    def test_05_competing_lines(self):
        """Selects line with highest point density among multiple lines."""
        points = [
            (0, 0), (1, 1), (2, 2), (3, 3),  # 4 points on y = x
            (0, 5), (1, 5), (2, 5)            # 3 points on y = 5
        ]
        self.assertEqual(find_best_line(points), (1.0, 0.0))


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.14 - Best Line\n{'='*75}")

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
    run_tests(TestBestLine)