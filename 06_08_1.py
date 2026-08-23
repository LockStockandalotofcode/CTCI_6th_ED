import math

def min_egg_drops(floors: int = 100, eggs: int = 2) -> int:
    """CTCI 6.8: Returns minimum number of drops needed in worst case to identify egg breaking floor."""
    # sum of x + x-1 + x-2 + x-3 ... 1 = 100
    # (x * (x + 1)) / 2  = 100, rounded up is the answer 
    # to keep number of drops consistent and balanced irrespective of whether egg breaks on drop 1 or not
    # since this is just to minimise the number of drops for the worst case
    # X is floor we must start at, to keep up with this strategy of balanced number of drops

    if floors <= 0:
        return 0
    if eggs <= 1:
        return floors # linear sequential search

    discriminant = 1 + 8 * floors
    x = (-1 + math.sqrt(discriminant)) / 2
    return math.ceil(x)

def run_egg_drop_tests():
    test_cases = [
        (100, 2, 14, "Standard CTCI 100 floors, 2 eggs -> 14 drops max"),
        (0, 2, 0, "0 floors -> 0 drops required"),
        (1, 2, 1, "1 floor, 2 eggs -> 1 drop"),
        (100, 1, 100, "100 floors, 1 egg -> 100 drops (Linear sequential search)"),
        (10, 2, 4, "10 floors, 2 eggs -> 4 drops max (x(x+1)/2 >= 10)"),
        (14, 2, 5, "14 floors, 2 eggs -> 5 drops max"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 6.8: EGG DROP TESTS")
    print("=" * 60)

    for i, (floors, eggs, expected, desc) in enumerate(test_cases, 1):
        try:
            res = min_egg_drops(floors, eggs)
            assert res == expected, f"Floors={floors}, Eggs={eggs}: Expected {expected} drops, got {res}"
            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(f"6.8 SUMMARY: {passed} PASSED | {failed} FAILED | Total: {len(test_cases)}")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_egg_drop_tests()