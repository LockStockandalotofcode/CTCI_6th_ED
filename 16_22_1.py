from enum import Enum
import unittest

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def turn_right(self) -> "Direction":
        # turn Clockwise
        return Direction((self.value + 1) % 4)

    def turn_left(self) -> "Direction":
        return Direction((self.value - 1) % 4)

class Ant:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = Direction.EAST

    def move_forward(self):
        if self.direction == Direction.NORTH:
            self.y += 1
        if self.direction == Direction.EAST:
            self.x += 1
        if self.direction == Direction.SOUTH:
            self.y -= 1
        if self.direction == Direction.WEST:
            self.x -= 1

class Board:
    def __init__(self):
        self.black_cells: set[tuple[int, int]] = set()
        self.ant = Ant()
        self.min_x = 0
        self.max_x = 0
        self.min_y = 0
        self.max_y = 0

    def _update_bounds(self):
        self.min_x = min(self.min_x, self.ant.x)
        self.max_x = max(self.max_x, self.ant.x)
        self.min_y = min(self.min_y, self.ant.y)
        self.max_y = max(self.max_y, self.ant.y)

    def step(self):
        pos = (self.ant.x, self.ant.y)
        is_black = pos in self.black_cells

        if is_black:
            self.ant.direction = self.ant.direction.turn_left()
            self.black_cells.remove(pos)
        else:
            self.ant.direction = self.ant.direction.turn_right()
            self.black_cells.add(pos)

        self.ant.move_forward()
        self._update_bounds()

    def simulate(self, k: int):
        for _ in range(k):
            self.step()

    def print_board(self) -> str:
        lines = []
        ant_symbol = {
            Direction.NORTH: "^",
            Direction.EAST: ">",
            Direction.SOUTH: "v",
            Direction.WEST: "<",
        }

        for y in range(self.max_y, self.min_y - 1, -1):
            row = []
            for x in range(self.min_x, self.max_x + 1):
                if x == self.ant.x and y == self.ant.y:
                    row.append(ant_symbol[self.ant.direction])
                elif (x, y) in self.black_cells:
                    row.append("X") # BLACK Square
                else:
                    row.append("_") # White Square
            lines.append("".join(row))

        return "\n".join(lines)

# WRAPPER FUNCTION (bridges class to test suite)
def langtons_ant(k: int) -> list[str]:
    # Adapter function that runs on board simulation and returns a list of row strings
    board = Board()
    board.simulate(k)
    return board.print_board().split("\n")


# =====================================================================
# TAILORED TEST SUITE
# =====================================================================
class TestLangtonsAnt(unittest.TestCase):

    def test_01_zero_moves(self):
        """0 moves returns grid containing only the initial ant facing right."""
        self.assertEqual(langtons_ant(0), [">"])

    def test_02_one_move(self):
        """1 move flips initial cell to black (X) and turns ant down (v)."""
        self.assertEqual(langtons_ant(1), ["X", "v"])

    def test_03_two_moves(self):
        """2 moves constructs a 2x2 bounding region with ant facing left (<)."""
        self.assertEqual(langtons_ant(2), ["_X", "<X"])

    def test_04_four_moves_loop_completion(self):
        """4 moves completes first 2x2 square loop with ant back at (0,0) facing right (>)."""
        self.assertEqual(langtons_ant(4), ["X>", "XX"])

    def test_05_bounding_box_expansion(self):
        """10 moves correctly expands bounding box and updates grid representation."""
        result = langtons_ant(10)
        self.assertTrue(len(result) >= 3)
        self.assertTrue(
            any(">" in row or "v" in row or "<" in row or "^" in row for row in result)
        )


# =====================================================================
# CONCISE SINGLE-LINE TEST RUNNER
# =====================================================================
def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 16.22 - Langton's Ant (Custom Board Solution)\n{'='*75}")

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
    run_tests(TestLangtonsAnt)