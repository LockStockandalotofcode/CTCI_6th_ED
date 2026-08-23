import math
from typing import List

def get_open_lockers(n: int = 100) -> List[int]:
    """CTCI 6.9: Returns 1-based indices of all open lockers after n toggling passes."""
    # numbers that have an odd number of factors remain open by then end of this 
    # like 1, 2, 4
    # all numbers (prime and not prime) except for squares have even number of factors

    largest_square = math.floor(math.sqrt(n))
    result = []
    for i in range(1, largest_square + 1):
        result.append(i ** 2)
    return result

def run_100_lockers_tests():
    test_cases = [
        (0, [], "0 lockers -> []"),
        (1, [1], "1 locker -> [1]"),
        (3, [1], "3 lockers -> [1]"),
        (4, [1, 4], "4 lockers -> [1, 4]"),
        (10, [1, 4, 9], "10 lockers -> [1, 4, 9]"),
        (
            100,
            [1, 4, 9, 16, 25, 36, 49, 64, 81, 100],
            "Standard CTCI 100 lockers -> All perfect squares <= 100",
        ),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 6.9: 100 LOCKERS TESTS")
    print("=" * 60)

    for i, (n, expected, desc) in enumerate(test_cases, 1):
        try:
            res = get_open_lockers(n)
            assert res is not None, "Function returned None"
            assert sorted(res) == sorted(expected), (
                f"For N={n}: Expected open lockers {expected}, got {res}"
            )

            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"6.9 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_100_lockers_tests()