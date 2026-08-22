def flip_bit_to_win(n: int) -> int:
    """CTCI 5.3: Max length sequence of 1s in 32-bit int achievable by flipping one 0."""
    # single pass bit shift
    n &= 0xFFFFFFFF # to reduce to the 32 lowest bits
    # 0xFFFFFFFF evaluates to (2 ** 31 - 1)
    if n == 0xFFFFFFFF:
        return 32

    current_len = 0
    prev_len = 0
    max_len = 0

    for _ in range(32):
        # n & 1, gives us the least significant bit
        if (n & 1) == 1:
            current_len += 1
        else:
            prev_len = 0 if (n & 2) == 0 else current_len
            # next bit (2nd last significant bit) is 0 also
            current_len = 0

        max_len = max(max_len, prev_len + current_len + 1)
        n = n >> 1 
        # pop the least significant bit
    return max_len

def run_flip_bit_to_win_tests():
    test_cases = [
        (1775, 8, "CTCI example: 1775 (0b11011101111)"),
        (0, 1, "All zeros (flipping one 0 yields sequence length 1)"),
        (-1, 32, "All ones / -1 in 32-bit two's complement"),
        (1, 2, "Single set bit (0b1)"),
        (7, 4, "Consecutive ones (0b111)"),
        (0b10101010, 3, "Alternating bit pattern"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 5.3: FLIP BIT TO WIN TESTS")
    print("=" * 60)

    for i, (n, expected, desc) in enumerate(test_cases, 1):
        try:
            res = flip_bit_to_win(n)
            assert res == expected, f"For n={n}: Expected {expected}, got {res}"
            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"5.3 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_flip_bit_to_win_tests()