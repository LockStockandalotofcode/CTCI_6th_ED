def pairwise_swap(n: int) -> int:
    """CTCI 5.7: Swaps odd and even bits in a 32-bit integer."""
    # to avoid negative 32-bit signed integers
    # this makes sure 32 bit positive integer
    n &= 0xFFFFFFFF
    
    # generate bit mask with 10101010, i.e., 1 at odd positions only
    # even mask is odd_mask right-shifted by 1
    # get the even position bits and odd position bits
    # then take OR after bitwise shifting even to right, odd to left 

    # odd_mask is 10101010 which is 0xAA in hexadecimal representation
    # 10 or 0xA is 0b 1010 in binary
    # for a 32 bit - integer we'd need 8 A's 0xAAAAAAAA
    odd_mask = 0xAAAAAAAA
    # even_mask = odd_mask >> 1
    even_mask = 0x55555555
    # odd_mask is 01010101 which is 0x55 in hexadecimal representation
    # 10 or 0x5 is 0b 0101 in binary

    odd_pos_bits = n & odd_mask
    even_pos_bits = n & even_mask

    return (odd_pos_bits >> 1 | even_pos_bits << 1)

    # Alternative
    # odd_pos_bits >>= 1
    # even_pos_bits <<= 1
    # return (odd_pos_bits | even_pos_bits)

def run_pairwise_swap_tests():
    test_cases = [
        (0, 0, "Zero input -> 0"),
        (1, 2, "1 (0b01) -> 2 (0b10)"),
        (2, 1, "2 (0b10) -> 1 (0b01)"),
        (10, 5, "10 (0b1010) -> 5 (0b0101)"),
        (0xAAAAAAAA, 0x55555555, "Alternating bits 0xAAAAAAAA -> 0x55555555"),
        (0x55555555, 0xAAAAAAAA, "Alternating bits 0x55555555 -> 0xAAAAAAAA"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 5.7: PAIRWISE SWAP TESTS")
    print("=" * 60)

    for i, (n, expected, desc) in enumerate(test_cases, 1):
        try:
            res = pairwise_swap(n)
            assert res == expected, f"Pairwise swap for {hex(n)}: Expected {hex(expected)}, got {hex(res)}"
            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(f"5.7 SUMMARY: {passed} PASSED | {failed} FAILED | Total: {len(test_cases)}")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_pairwise_swap_tests()