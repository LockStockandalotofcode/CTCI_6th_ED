import math
import random
from typing import List, Tuple, Optional

def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

def is_coprime(a: int, b: int) -> bool:
    return gcd(a, b) == 1

def can_measure_water(jug1: int, jug2: int, target: int) -> bool:
    """CTCI 6.5: Returns True if target volume can be measured using jugs of jug1 and jug2 capacity."""
    # if the jug sizes are relatively prime, then you can measure any value between one and the sum of the jug sizes.
    # two numbers relatively prime or coprime -> gcd is 1
    if 0 > target or target > (jug1 + jug2):
        return False
    if target == 0:
        return True

    return (target % gcd(jug1, jug2) )== 0

def run_jugs_of_water_tests():
    test_cases = [
        (5, 3, 4, True, "Classic CTCI problem: 5-quart & 3-quart jugs -> 4 quarts"),
        (5, 3, 9, False, "Target exceeds combined individual jug capacities"),
        (0, 5, 3, False, "One jug has 0 capacity"),
        (6, 4, 3, False, "Target is not divisible by GCD(6, 4) = 2"),
        (6, 4, 2, True, "Target is divisible by GCD(6, 4) = 2"),
        (5, 3, 0, True, "Target volume is 0 quarts"),
        (5, 5, 5, True, "Target equals jug capacity"),
        (3, 5, 5, True, "Target equals larger jug capacity"),
    ]

    passed, failed = 0, 0
    print("\n" + "=" * 60)
    print("RUNNING CTCI 6.5: JUGS OF WATER TESTS")
    print("=" * 60)

    for i, (j1, j2, target, expected, desc) in enumerate(test_cases, 1):
        try:
            res = can_measure_water(j1, j2, target)
            assert res == expected, f"Jugs({j1}, {j2}) for target {target}: Expected {expected}, got {res}"
            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(f"6.5 SUMMARY: {passed} PASSED | {failed} FAILED | Total: {len(test_cases)}")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_jugs_of_water_tests()