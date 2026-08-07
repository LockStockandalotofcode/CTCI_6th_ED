from typing import Optional, List, Tuple, Set, Callable, Dict
import itertools
import math

# Concept
# taking 1 from bottle 1, 2 from bottle 2, and so on, n pills from bottle n
# if all had been same 1g bottles, we'd have had (20 * 21) / 2 = 210 gm weight
# whatever extra to this 210, divided by 0.1 gm, gives no. of 1.1 pills are used which is the same as the bottle no. of the bottle with heavier pills

def find_heavy_bottle(
    num_bottles: int,
    scale_fn: Callable[[List[int]], float],
    normal_weight: float = 1.0,
    pill_diff: float = 0.1,
) -> int:
    # Identifies the 0-indexed heavy bottle by calling scale_fn EXACTLY ONCE.
    # scale_fn accepts a list of integers representing the count of pills taken from each bottle [count_0, count_1, ..., count_N-1] and returns total weight.

    pills_per_bottle_list = [i for i in range(1, num_bottles + 1)]
    total_weight = scale_fn(pills_per_bottle_list)
    expected_weight = normal_weight * ((num_bottles * (num_bottles + 1)) / 2)
    extra_weight = (total_weight - expected_weight)
    heavier_bottle_index = round(extra_weight / pill_diff) - 1
    # never use // floor division with floating point numbers, instead use round()
    # subtract 1 from index_calculation to get the right 0-indexed bottle number
    # since im using i+1 pills for bottle with index i 
    # the test case is identifying against 0-based index of the bottle
    return int(heavier_bottle_index)

class SingleUseScale:

    def __init__(
        self,
        num_bottles: int,
        heavy_bottle_idx: int,
        normal_weight: float = 1.0,
        pill_diff: float = 0.1,
    ):
        self.num_bottles = num_bottles
        self.heavy_idx = heavy_bottle_idx
        self.normal_weight = normal_weight
        self.pill_diff = pill_diff
        self.call_count = 0

    def weigh(self, pill_counts: List[int]) -> float:
        self.call_count += 1
        if self.call_count > 1:
            raise RuntimeError(
                "VIOLATION: Scale scale_fn was called more than ONCE!"
            )

        if len(pill_counts) != self.num_bottles:
            raise ValueError(
                f"Expected pill counts for {self.num_bottles} bottles, got"
                f" {len(pill_counts)}"
            )

        total_weight = 0.0
        for idx, count in enumerate(pill_counts):
            w = (
                self.normal_weight + self.pill_diff
                if idx == self.heavy_idx
                else self.normal_weight
            )
            total_weight += count * w

        return round(total_weight, 6)


def run_heavy_pill_tests():
    # Format: (num_bottles, heavy_bottle_index, normal_weight, pill_diff)
    test_cases = [
        (20, 0, 1.0, 0.1),  # Heavy bottle at index 0
        (20, 19, 1.0, 0.1),  # Heavy bottle at last index
        (20, 10, 1.0, 0.1),  # Heavy bottle in middle
        (5, 2, 1.0, 0.1),  # Smaller bottle set
        (100, 73, 5.0, 0.2),  # Scaled up scale parameters & non-standard weights
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 6.1: THE HEAVY PILL TESTS")
    print("=" * 60)

    for i, (n_bottles, heavy_idx, norm_w, diff) in enumerate(test_cases, 1):
        scale = SingleUseScale(n_bottles, heavy_idx, norm_w, diff)
        try:
            found_idx = find_heavy_bottle(
                n_bottles, scale.weigh, normal_weight=norm_w, pill_diff=diff
            )

            assert scale.call_count == 1, (
                "Scale was never called or called multiple times!"
                f" Count: {scale.call_count}"
            )
            assert found_idx == heavy_idx, (
                f"Expected heavy bottle index {heavy_idx}, got {found_idx}"
            )

            print(
                f"  [PASS] Test {i:02d}: {n_bottles} Bottles | Heavy Index:"
                f" {heavy_idx} Identified in 1 Weighing"
            )
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"6.1 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_heavy_pill_tests()