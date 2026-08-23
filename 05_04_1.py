import math
from typing import Optional, Tuple, Union

# --- Data Structures & Function Contracts ---
def get_next_larger(n: int) -> Union[int, None]:
    """CTCI 5.4: Finds the smallest integer > n with the same number of 1 bits.

    Returns -1 or None if no such positive 32-bit integer exists.
    """
    if n <= 0:
        return -1

    # get pos p of first non-trailing zero,
    # get number of 1s and 0s to p's right
    # flip bit p to 1, insert (c1 - 1) 1s to rightmost bits, starting at the least significant bit
    temp, c0, c1 = n, 0, 0
    # clear all trailing 0s
    while (temp & 1) ==0 and temp != 0:
        c0 += 1
        temp >>= 1
    # clear all 1s to the left of trailing zeroes
    while (temp & 1) ==1:
        c1 += 1
        temp >>= 1

    p = c0 + c1
    # early return if out of bounds  
    if p == 31 or p == 0:
        return -1

    # flip bit p
    n  = n | (1 << p)
    # clear all bits right of p
    # ~ flips all bits of any number
    n = n & ~((1 << p) - 1)
    # insert c1 - 1 1s at far right
    n = n | ((1 << (c1 - 1)) - 1)
    return n

def get_next_smaller(n: int) -> Union[int, None]:
    """CTCI 5.4: Finds the largest integer < n with the same number of 1 bits.

    Returns -1 or None if no such positive integer exists.
    """
    if n <= 0:
        return -1
    # get pos p of first non-trailing one
    # get number of 1s and 0s to p's right
    # flip bit at p to 0, insert (c1 - 1) bits immediately to right of p
    temp, c0, c1 = n, 0, 0
    # clear all trailing  1s 
    while (temp & 1) ==1:
        c1 += 1
        temp >>= 1
    if temp == 0:
        return -1
    # clear all trailing 0s
    while (temp & 1) ==0 and temp != 0:
        c0 += 1
        temp >>= 1

    p = c0 + c1
    n = n & (~0 << (p + 1)) # clearing all bits from 0 to p, including p
    # insert (c1 + 1) 1 bits to immediate right of p
    mask = ((1 << (c1 + 1)) - 1) << (c0 - 1)
    n = n | mask
    return n

def get_next_number(n: int) -> Tuple[Union[int, None], Union[int, None]]:
    """CTCI 5.4: Combined function returning tuple (next_smaller, next_larger)."""
    return (get_next_smaller(n), get_next_larger(n))

def run_next_number_tests():
    # Verification helpers using ground-truth brute force
    def count_ones(x: int) -> int:
        return bin(x).count("1") if x > 0 else 0

    def expected_next_larger(x: int, max_bits: int = 31) -> int:
        if x <= 0:
            return -1
        target_count = count_ones(x)
        curr = x + 1
        limit = (1 << max_bits) - 1
        while curr <= limit:
            if count_ones(curr) == target_count:
                return curr
            curr += 1
        return -1

    def expected_next_smaller(x: int) -> int:
        if x <= 0:
            return -1
        target_count = count_ones(x)
        curr = x - 1
        while curr > 0:
            if count_ones(curr) == target_count:
                return curr
            curr -= 1
        return -1

    test_cases = [
        (12, "Standard case 12 (0b1100 -> larger: 17 [0b10001], smaller: 10 [0b1010])"),
        (5, "Standard case 5 (0b101 -> larger: 6 [0b110], smaller: 3 [0b011])"),
        (13948, "CTCI book example 13948"),
        (1, "Single bit (0b1 -> larger: 2, smaller: impossible)"),
        (7, "All trailing ones (0b111 -> larger: 11, smaller: impossible)"),
        (16, "Power of 2 (0b10000 -> larger: 32, smaller: 8)"),
        (23, "Bit pattern with internal zeros (0b10111)"),
        (0, "Edge case n = 0 (No positive ones -> both impossible)"),
        (-5, "Edge case negative number (Out of positive scope -> both impossible)"),
        (1073741823, "Large 30-bit integer with all 1s ((1<<30)-1)"),
    ]

    passed, failed = 0, 0
    print("\n" + "=" * 60)
    print("RUNNING CTCI 5.4: NEXT NUMBER TESTS")
    print("=" * 60)

    for i, (n, desc) in enumerate(test_cases, 1):
        try:
            exp_larger = expected_next_larger(n)
            exp_smaller = expected_next_smaller(n)

            # Test individual function or combined function
            res_larger = get_next_larger(n)
            res_smaller = get_next_smaller(n)

            # Fallback check if user implemented combined tuple function
            if res_larger is None and res_smaller is None:
                comb_res = get_next_number(n)
                if comb_res is not None:
                    res_smaller, res_larger = comb_res

            # Normalize None responses to -1 for standard comparison
            norm_larger = -1 if res_larger is None else res_larger
            norm_smaller = -1 if res_smaller is None else res_smaller

            # Assert Next Larger Correctness
            assert norm_larger == exp_larger, (
                f"For n={n} ({bin(n) if n > 0 else n}): Next Larger expected {exp_larger}, got {res_larger}"
            )

            # Assert Next Smaller Correctness
            assert norm_smaller == exp_smaller, (
                f"For n={n} ({bin(n) if n > 0 else n}): Next Smaller expected {exp_smaller}, got {res_smaller}"
            )

            # Additional Bit-Weight Verification Check (if valid number returned)
            if norm_larger != -1:
                assert count_ones(norm_larger) == count_ones(n), (
                    f"Bit count mismatch for larger: {count_ones(norm_larger)} != {count_ones(n)}"
                )
            if norm_smaller != -1:
                assert count_ones(norm_smaller) == count_ones(n), (
                    f"Bit count mismatch for smaller: {count_ones(norm_smaller)} != {count_ones(n)}"
                )

            print(f"  [PASS] Test {i:02d}: {desc}")
            print(f"         n={n} | Smaller: {norm_smaller} | Larger: {norm_larger}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(f"5.4 SUMMARY: {passed} PASSED | {failed} FAILED | Total: {len(test_cases)}")
    print("=" * 60 + "\n")


if __name__ == "__main__":    run_next_number_tests()