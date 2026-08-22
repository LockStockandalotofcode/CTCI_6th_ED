from typing import List

def find_duplicates(arr: List[int], max_val: int = 32000) -> List[int]:
    """CTCI 10.8: Finds duplicate numbers in [1, max_val] using bit vector logic."""

    #  1. scan the list, use 4KB bitvector, covers 1 to 32 * (2 ^ 10); 32 * (10 ^ 3) is less than this, so easily covered 
    bitvector = bytearray((max_val // 8) + 1)
    dups = []
    for num in arr:
        # breakpoint()
        byte_idx = num // 8
        bit_idx = num % 8
        if (bitvector[byte_idx] & (1 << (bit_idx))) == 0: # get_bit
            bitvector[byte_idx] |= (1 << bit_idx) # set_bit
        else:
            dups.append(num)

    return dups

def run_find_duplicates_tests():
    test_cases = [
        ([], [], "Empty input array"),
        ([1, 2, 3, 4, 5], [], "Array without duplicates"),
        (
            [1, 2, 2, 3, 4, 4, 5],
            [2, 4],
            "Standard array with distinct duplicates",
        ),
        ([7, 7, 7, 7], [7], "Single value repeated multiple times"),
        (
            [1, 32000, 32000, 1],
            [1, 32000],
            "Duplicates at min and max boundary values",
        ),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 10.8: FIND DUPLICATES TESTS")
    print("=" * 60)

    for i, (arr, expected_dups, desc) in enumerate(test_cases, 1):
        try:
            res = find_duplicates(arr)
            assert set(res) == set(
                expected_dups
            ), f"Expected unique duplicates {set(expected_dups)}, got {set(res)}"
            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"10.8 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_find_duplicates_tests()