import unittest
from typing import Optional, Tuple

Point = tuple[float, float]

def _is_between(start: float, middle: float, end: float) -> bool:
    # check if middle value lies between start and end, (inclusive)
    return min(start, end) - 1e-9 <= middle <= max(start, end) + 1e-9

def _is_point_on_segment(p: Point, seg_start: Point, seg_end: Point) -> bool:
    # checks if point p lies within boudaries of given segment
    return (_is_between(seg_start[0], p[0], seg_end[0]) and _is_between(seg_start[1], p[1], seg_end[1]))

def _compute_line_parameters(p1: Point, p2: Point) -> tuple[Optional[float], float]:
    # helper compute slope m, intercept c, for line segment p1, p2
    # returns (None, x1) if line is vertical
    # 1e-9 is floating  point 1 * 10^ (-9)
    if abs(p1[0] - p2[0]) < 1e-9:
        return (None, p1[0]) # vertical line
    m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    c = p1[1] - m * (p1[0])
    return (m, c)

def find_intersection(start1: Point, end1: Point, start2: Point, end2: Point) -> Optional[Point]:
    # Computes intersection point of two line segments, if exists.
    # Time: O(1), Auxiliary space: O(1)

    m1, c1 = _compute_line_parameters(start1, end1)
    m2, c2 = _compute_line_parameters(start2, end2)

    # Case 1: both lines vertical
    if m1 is None and m2 is None:
        # check for collinearity
        if abs(c1 - c2) < 1e-9: # Same x-coordinate
            # check overlap on y-axis
            if _is_point_on_segment(start1, start2, end2):
                return start1
            if _is_point_on_segment(start2, start1, end1):
                return start2
        return None
        
    # Case 2: one line is vertical
    # A - line 1 is vertical, line 2 is not
    if m1 is None:
        # vertical line, equation
        x = c1
        # y - intercept 
        y = m2 * x + c2
        intersect_pt = (x, y)

        if _is_point_on_segment(intersect_pt, start1, end1) and _is_point_on_segment(intersect_pt, start2, end2):
            return intersect_pt
            
        return None
        
    # B - line 2 is vertical, line 1 is not
    if m2 is None:
        # vertical line, equation
        x = c2
        # y - intercept 
        y = m1 * x + c1
        intersect_pt = (x, y)

        if _is_point_on_segment(intersect_pt, start1, end1) and _is_point_on_segment(intersect_pt, start2, end2):
            return intersect_pt

        return None
        
    # Case 3: parallel non-vertical lines
    # since m1, m2 are floating points, they migh not be exact, so == doesnt always work
    if abs(m1 - m2) < 1e-9:
        if abs(c1 - c2) < 1e-9: # collinear or not
            if _is_point_on_segment(start1, start2, end2):
                return start1
            if _is_point_on_segment(start2, start1, end1):
                return start2
        return None
        
    # Case 4: non-parallel non-vertical lines, check for intersection point on the segments
    x = (c2 - c1) / (m1 - m2)
    y = m1 * x + c1 
    intersect_pt = (x, y)

    if _is_point_on_segment(intersect_pt, start1, end1) and _is_point_on_segment(intersect_pt, start2, end2):
        return intersect_pt
    return None

# =====================================================================
# TEST SUITE
# =====================================================================
class TestIntersection(unittest.TestCase):

    def test_01_standard_intersection(self):
        """Two perpendicular segments intersecting at (0, 0)."""
        p1, p2 = (-1.0, 0.0), (1.0, 0.0)
        p3, p4 = (0.0, -1.0), (0.0, 1.0)
        self.assertEqual(find_intersection(p1, p2, p3, p4), (0.0, 0.0))

    def test_02_parallel_non_intersecting(self):
        """Parallel horizontal segments do not intersect."""
        p1, p2 = (0.0, 0.0), (2.0, 0.0)
        p3, p4 = (0.0, 1.0), (2.0, 1.0)
        self.assertIsNone(find_intersection(p1, p2, p3, p4))

    def test_03_lines_intersect_outside_segments(self):
        """Infinite lines intersect, but line segments do not reach each other."""
        p1, p2 = (0.0, 0.0), (1.0, 1.0)
        p3, p4 = (3.0, 0.0), (4.0, -1.0)
        self.assertIsNone(find_intersection(p1, p2, p3, p4))

    def test_04_endpoint_intersection(self):
        """Segments touching at an exact shared endpoint."""
        p1, p2 = (0.0, 0.0), (2.0, 2.0)
        p3, p4 = (2.0, 2.0), (4.0, 0.0)
        self.assertEqual(find_intersection(p1, p2, p3, p4), (2.0, 2.0))

    def test_05_floating_point_intersection(self):
        """Non-integer coordinate intersection."""
        p1, p2 = (0.0, 0.0), (2.0, 2.0)
        p3, p4 = (0.0, 2.0), (2.0, 0.0)
        self.assertEqual(find_intersection(p1, p2, p3, p4), (1.0, 1.0))


# =====================================================================
# CONCISE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.3 - Intersection\n{'='*75}")

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
    run_tests(TestIntersection)