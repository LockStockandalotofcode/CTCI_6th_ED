# only hint1 
def recursive_multiply(num1: int, num2: int) -> int:
    if not num1 or not num2: return 0

    result = 0
    # keeping num2 as the smaller one, and num1 as the bigger one
    if num1 < num2:
        num2, num1 = num1, num2

    for _ in range(num2):
        result += num1

    return result

def run_recursive_multiply_tests():
    test_cases = [
        # (a, b, expected)
        (0, 5, 0),
        (5, 0, 0),
        (1, 10, 10),
        (10, 1, 10),
        (7, 8, 56),
        (31, 15, 465),
        (100, 25, 2500),
        (1234, 5678, 7006652),
    ]

    passed, failed = 0, 0
    print("\n" + "=" * 60)
    print("RUNNING CTCI 8.5: RECURSIVE MULTIPLY TESTS")
    print("=" * 60)

    for i, (a, b, expected) in enumerate(test_cases, 1):
        try:
            res = recursive_multiply(a, b)
            assert (
                res == expected
            ), f"For {a} * {b}, expected {expected}, got {res}"
            print(f"  [PASS] Test {i:02d}: {a} * {b} -> {res}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {a} * {b} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"8.5 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_recursive_multiply_tests()