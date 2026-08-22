from typing import List

# LIS style DP
# bottom-up dp array solution

class Box:
    def __init__(self, w: int, h: int, d: int):
        self.w = w
        self.h = h
        self.d = d

    def __repr__(self):
        return (f"Box(w={self.w}, h={self.h}, d={self.d})")

def can_place(top: Box, bottom: Box)-> bool:
    return True if (top.w < bottom.w and top.h < bottom.h and top.d < bottom.d) else False

def max_stack_height(boxes: List[Box]) -> int:
    """CTCI 8.13: Max height of strictly decreasing dimension box stack."""
    # empty case
    if not boxes:
        return 0

    # 1. Sort boxes by width, sort() method sorts in-place, mutating original list, setting up custom comparator and in decresing length
    # breakpoint()
    boxes.sort(key=lambda b: b.w, reverse=True)
    n = len(boxes)

    # dp[i] stores max_height stack for sequence 0 to i, having box[i] on top
    dp = [box.h for box in boxes]

    # LIS style DP
    for i in range(n):
        for j in range(i):
            if can_place(boxes[i], boxes[j]):
                dp[i] = max(dp[i], dp[j] + boxes[i].h)

    # final answer is the maximum amongst the dp array values
    return max(dp)

def run_stack_of_boxes_tests():
    test_cases = [
        ([], 0, "Empty list of boxes"),
        ([Box(4, 5, 6)], 5, "Single box"),
        (
            [Box(5, 5, 5), Box(5, 5, 5)],
            5,
            "Identical dimensions (cannot stack strictly equal boxes)",
        ),
        (
            [Box(1, 1, 1), Box(2, 2, 2), Box(3, 3, 3)],
            6,
            "Strictly increasing dimensions (1+2+3 = 6)",
        ),
        (
            [Box(10, 1, 1), Box(1, 10, 1), Box(1, 1, 10)],
            10,
            "Incompatible dimensions (max single height = 10)",
        ),
        (
            [Box(6, 6, 6), Box(5, 4, 5), Box(4, 5, 4)],
            11,
            "Branch choice optimization (6+5=11)",
        ),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 8.13: STACK OF BOXES TESTS")
    print("=" * 60)

    for i, (boxes, expected_height, desc) in enumerate(test_cases, 1):
        try:
            res = max_stack_height(boxes)
            assert res == expected_height, (
                f"Expected max height {expected_height}, got {res}"
            )
            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"8.13 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_stack_of_boxes_tests()