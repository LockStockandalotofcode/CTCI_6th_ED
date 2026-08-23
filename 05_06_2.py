def bit_swap_required(a: int, b: int) -> int:
    """CTCI 5.6: Returns number of bit flips needed to convert integer A to integer B."""
    # XOR gives the bits that are different in the two numbers
    # count the number of bits in XOR of the two numbers
    c = a ^ b
    diff_bits = 0
    # slightly better, remove all contiguous 0s in c all at once
    # this is done by c & (c - 1)
    # then it just iterates for the number of 1s in c, which is the answer, so we just track how many iteration until c is 0
    while c != 0:
        diff_bits += 1 # gives us the least significant bit - 1 or 0
        c = c & (c - 1)

    return diff_bits

def run_conversion_tests():
    test_cases = [
        (29, 15, 2, "CTCI example: 29 (11101) to 15 (01111) -> 2 bits"),
        (0, 0, 0, "Identical zero inputs -> 0 bits"),
        (15, 15, 0, "Identical non-zero inputs -> 0 bits"),
        (0, 15, 4, "Converting 0 to 15 (01111) -> 4 bits"),
        (0b101010, 0b010101, 6, "Completely inverted 6-bit pattern -> 6 bits"),
        (0xFFFFFFFF, 0x00000000, 32, "32-bit inverted integers -> 32 bits"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 5.6: CONVERSION TESTS")
    print("=" * 60)

    for i, (a, b, expected, desc) in enumerate(test_cases, 1):
        try:
            res = bit_swap_required(a, b)
            assert res == expected, f"Bit swap between {a} and {b}: Expected {expected}, got {res}"
            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(f"5.6 SUMMARY: {passed} PASSED | {failed} FAILED | Total: {len(test_cases)}")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_conversion_tests()