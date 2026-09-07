import unittest
from typing import Tuple

class Point:

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def to_tuple(self) -> tuple[float, float]:
        return (self.x, self.y)

class Square:
    def __init__(self, left: float, top: float, size: float): 
        self.left = left
        self.top = top
        self.right = left + size
        self.bottom = top + size
        self.size = size

    def center(self) -> Point:
        # calculates center coordinates of square
        return Point(self.left + self.size / 2.0, self.top + self.size / 2.0)

class Line:

    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1
        self.p2 = p2

def _get_boundary(center1: Point, center2: Point, s1: Square, s2: Square) -> Line:
    # Helper returns boundary (line segment coordinates), of biscting line
    # Handle vertical line, in case of both squares have same x-coordinate in center
    if center1.x == center2.x:
        top_y = min(s1.top, s2.top)
        bottom_y = max(s1.bottom, s2.bottom)
        return Line(Point(center1.x, top_y), Point(center2.x, bottom_y))

    # Determine outer x-boundaries
    x_left = min(s1.left, s2.left)
    x_right = max(s1.right, s2.right)

    slope = (center2.y - center1.y) / (center2.x - center1.x)
    # y = m(x - x1) + y1
    # line equation
    y_left = slope * (x_left - center1.x) + center1.y
    y_right = slope * (x_right - center1.x) + center1.y

    return Line(Point(x_left, y_left), Point(x_right, y_right))

def find_bisecting_line(s1: Square, s2: Square) -> Line:
    # Bisecting line always passes throguh both squares' centers
    # so we find Center connecting line
    # then for line segment, find its itersections with the enclosing boundary of the squares
    c1 = s1.center()
    c2 = s2.center()

    # if same center (Concentric squares), cut vertically through shared center
    if c1.x == c2.x and c1.y == c2.y:
        return Line(Point(c1.x, s1.top), Point(c1.x, s1.bottom))

    return _get_boundary(c1, c2, s1, s2)




    

# =====================================================================
# TEST SUITE
# =====================================================================
class TestBisectSquares(unittest.TestCase):

    def test_01_concentric_squares(self):
        """Concentric squares line spans outer square vertically through center."""
        s1 = Square(0, 0, 10)  # center (5, 5), top 0, bottom 10
        s2 = Square(2, 2, 6)  # center (5, 5)
        # breakpoint()
        line = find_bisecting_line(s1, s2)

        self.assertEqual(line.p1.to_tuple(), (5.0, 0.0))
        self.assertEqual(line.p2.to_tuple(), (5.0, 10.0))

    def test_02_horizontally_aligned_squares(self):
        """Horizontally aligned squares form a horizontal bisecting line."""
        s1 = Square(0, 0, 4)  # center (2, 2), left 0
        s2 = Square(10, 0, 4)  # center (12, 2), right 14
        line = find_bisecting_line(s1, s2)

        self.assertEqual(line.p1.to_tuple(), (0.0, 2.0))
        self.assertEqual(line.p2.to_tuple(), (14.0, 2.0))
        self.assertEqual(line.p1.y, line.p2.y)

    def test_03_vertically_aligned_squares(self):
        """Vertically aligned squares form a vertical bisecting line."""
        s1 = Square(0, 0, 4)  # center (2, 2), top 0
        s2 = Square(0, 10, 4)  # center (2, 12), bottom 14
        line = find_bisecting_line(s1, s2)

        self.assertEqual(line.p1.to_tuple(), (2.0, 0.0))
        self.assertEqual(line.p2.to_tuple(), (2.0, 14.0))
        self.assertEqual(line.p1.x, line.p2.x)

    def test_04_diagonally_placed_squares(self):
        """Diagonally placed squares calculate distinct boundary endpoints."""
        s1 = Square(0, 0, 2)  # center (1, 1), left 0
        s2 = Square(4, 4, 4)  # center (6, 6), right 8
        line = find_bisecting_line(s1, s2)

        self.assertEqual(line.p1.to_tuple(), (0.0, 0.0))
        self.assertEqual(line.p2.to_tuple(), (8.0, 8.0))


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.13 - Bisect Squares\n{'='*75}")

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
    run_tests(TestBisectSquares)