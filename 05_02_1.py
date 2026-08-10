import math

# double to binary
# input = 0.72
# binary rep_n of 72
# 0.72 = 72 / (10 ^ 2); 2 is number of significant digits

# HINT 1
# converting positive integer to its binary representation
def binary_rep(num: int) -> int:
    if num < 0: return None

    curr = num
    binary = 0b0
    while curr > 0:
        greatest_power_of_two = int(math.log(curr, 2))
        binary += (10 ** greatest_power_of_two)
        # 1 << p, computes 2^p in the base - 10
        curr = curr % (2 ** greatest_power_of_two)

    return binary

def run_binary_rep_tests():
    # Format: (input_num, description)
    test_cases = [
        (0, "Zero boundary case"),
        (1, "Smallest positive integer (2^0)"),
        (2, "Power of two (2^1 -> 10)"),
        (5, "Odd number (5 -> 101)"),
        (8, "Power of two floating-point edge case (8 -> 1000)"),
        (10, "Even non-power of two (10 -> 1010)"),
        (15, "All ones representation (15 -> 1111)"),
        (23, "General composite number (23 -> 10111)"),
        (64, "Larger power of two (64 -> 1000000)"),
        (-5, "Negative number (returns None)"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING BINARY REPRESENTATION TESTS")
    print("=" * 60)

    for i, (num, desc) in enumerate(test_cases, 1):
        try:
            res = binary_rep(num)

            # Ground truth generation using built-in bin()
            if num < 0:
                expected = None
            elif num == 0:
                expected = 0
            else:
                expected = int(bin(num)[2:])

            assert res == expected, (
                f"For input {num}: Expected {expected}, got {res}"
            )

            print(f"  [PASS] Test {i:02d}: {desc} ({num} -> {res})")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"SUMMARY: {passed} PASSED | {failed} FAILED | Total: {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_binary_rep_tests()