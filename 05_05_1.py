def is_power_of_two_or_zero(n: int) -> bool:
    """CTCI 5.5: Evaluates bitwise expression ((n & (n - 1)) == 0)."""
    # should evaluate to True only for n = powers of 2
    return (n & (n - 1)) == 0

def run_debugger_tests():
    test_cases = [
        (0, True, "n = 0 -> True (0 & -1 == 0)"),
        (1, True, "n = 1 -> True (Power of 2: 2^0)"),
        (2, True, "n = 2 -> True (Power of 2: 2^1)"),
        (16, True, "n = 16 -> True (Power of 2: 2^4)"),
        (1024, True, "n = 1024 -> True (Power of 2: 2^10)"),
        (15, False, "n = 15 -> False (Not a power of 2)"),
        (3, False, "n = 3 -> False (Not a power of 2)"),
        (1023, False, "n = 1023 -> False (Not a power of 2)"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 5.5: DEBUGGER TESTS")
    print("=" * 60)

    for i, (n, expected, desc) in enumerate(test_cases, 1):
        try:
            res = is_power_of_two_or_zero(n)
            assert res == expected, f"For n={n}: Expected {expected}, got {res}"
            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(f"5.5 SUMMARY: {passed} PASSED | {failed} FAILED | Total: {len(test_cases)}")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_debugger_tests()