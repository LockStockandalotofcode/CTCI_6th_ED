def days_for_blue_eyes_to_leave(num_blue_eyed: int) -> int:
    """CTCI 6.6: Returns the number of days required for all blue-eyed people to leave the island."""
    return num_blue_eyed

def run_blue_eyes_tests():
    test_cases = [
        (0, 0, "0 blue-eyed people -> 0 days"),
        (1, 1, "1 blue-eyed person -> 1 day"),
        (2, 2, "2 blue-eyed people -> 2 days"),
        (5, 5, "5 blue-eyed people -> 5 days"),
        (100, 100, "100 blue-eyed people -> 100 days"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 6.6: BLUE EYES TESTS")
    print("=" * 60)

    for i, (n, expected, desc) in enumerate(test_cases, 1):
        try:
            res = days_for_blue_eyes_to_leave(n)
            assert res == expected, f"For {n} blue-eyed people: Expected {expected} days, got {res}"
            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(f"6.6 SUMMARY: {passed} PASSED | {failed} FAILED | Total: {len(test_cases)}")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_blue_eyes_tests()