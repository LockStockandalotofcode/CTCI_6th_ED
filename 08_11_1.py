from typing import Optional

def make_change(n: int, denoms: Optional[list[int]] = None) -> int:
    if n < 0: 
        return 0
    if denoms is None:
        denoms = [25, 10, 5, 1]
    return make_change_helper(n, denoms, 0)

def make_change_helper(amount: int, denoms: list[int], index: int) -> int:
    if index >= len(denoms) - 1:
        return 1 if amount % denoms[index] == 0 else 0
         # base case - fully reduced statement

    combinations = 0
    curr_denom = denoms[index]
    i = 0
    while (i * curr_denom) <= amount: 
        amount_remaining = amount - (i * curr_denom)
        combinations += make_change_helper(amount_remaining, denoms, index + 1)
        i += 1

    return combinations

def run_coins_tests():
    test_cases = [
        (0, [25, 10, 5, 1], 1, "0 cents -> 1 valid way (0 coins)"),
        (-10, [25, 10, 5, 1], 0, "Negative cents -> 0 ways"),
        (1, [25, 10, 5, 1], 1, "1 cent -> 1 way ([1])"),
        (5, [25, 10, 5, 1], 2, "5 cents -> 2 ways ([5], [1*5])"),
        (10, [25, 10, 5, 1], 4, "10 cents -> 4 ways"),
        (25, [25, 10, 5, 1], 13, "25 cents -> 13 ways"),
        (100, [25, 10, 5, 1], 242, "100 cents -> 242 ways"),
        (7, [2, 3], 1, "Custom coin set [2, 3] for n=7 (3+2+2) -> 1 way"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 8.11: COINS TESTS")
    print("=" * 60)

    for i, (n, coins, expected, desc) in enumerate(test_cases, 1):
        try:
            res = make_change(n, coins)
            assert res == expected, f"For n={n} cents: Expected {expected} ways, got {res}"
            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(f"8.11 SUMMARY: {passed} PASSED | {failed} FAILED | Total: {len(test_cases)}")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_coins_tests()