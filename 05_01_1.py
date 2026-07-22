# LOGIC & CODE
# build a clearing mask, from index i through j, 0s rest all 1s(infinite length), taking & of n with mask, clears the bits from i to j
# then | of m and n gives the result
def insert_bits(n: int, m: int, i: int, j: int) -> int:
    # making the MASK
    # ones to left of index j
    ones_to_left = -1 << (j + 1) # this operator shifts by j+1 places, so from index j: its all 0
    ones_to_right = (1 << i) - 1 # creating fixed i-length number of all 1s
    mask = ones_to_left | ones_to_right

    # clear i to j bits in n
    n = n & mask

    # shift bits  of m by i places to left, before merging
    m = m << i

    # put m's bits in i to j
    n = n | m

    return n

# =====================================================================
# PART 2: UNIVERSAL TEST TEMPLATE (DO NOT EDIT)
# =====================================================================

def run_tests(insert_function):
    print(f"Running Universal Test Suite for 5.1 Insertion:\n")
    all_passed = True

    # -------------------------------------------------------------
    # Test 1: Standard Case (The CTCI Book Example)
    # -------------------------------------------------------------
    try:
        # N = 10000000000 (1024 in decimal)
        # M = 10011 (19 in decimal)
        # i = 2, j = 6
        # Expected = 10001001100 (1100 in decimal)
        result = insert_function(1024, 19, 2, 6)
        if result == 1100:
            print("Passed Test 1: Standard bit insertion works correctly.")
        else:
            print(f"FAILED Test 1: Expected 1100, got {result}. Check your shift alignment.")
            all_passed = False
    except Exception as e:
        print(f"FAILED Test 1 with error: {e}")
        all_passed = False

    # -------------------------------------------------------------
    # Test 2: Edge Case - Inserting Zeroes (The Clearing Mask Test)
    # -------------------------------------------------------------
    try:
        # If your clearing mask is wrong, this test will fail.
        # N = 11111 (31 in decimal)
        # M = 0
        # i = 1, j = 3
        # Expected = 10001 (17 in decimal) -> Bits 1, 2, and 3 must be zeroed out.
        result = insert_function(31, 0, 1, 3)
        if result == 17:
            print("Passed Test 2: Proper clearing mask applied before insertion.")
        else:
            print(f"FAILED Test 2: Expected 17, got {result}. You might be using an OR operator without clearing the bits in N first.")
            all_passed = False
    except Exception as e:
        print(f"FAILED Test 2 with error: {e}")
        all_passed = False

    # -------------------------------------------------------------
    # Test 3: Boundary Case - Inserting at the absolute edge (i = 0)
    # -------------------------------------------------------------
    try:
        # N = 1010 (10 in decimal)
        # M = 1 (1 in decimal)
        # i = 0, j = 1
        # Expected = 1001 (9 in decimal) -> Overwriting the last two bits.
        result = insert_function(10, 1, 0, 1)
        if result == 9:
            print("Passed Test 3: Edge boundary (i=0) handled correctly.")
        else:
            print(f"FAILED Test 3: Expected 9, got {result}. Check off-by-one errors in your bit mask generation.")
            all_passed = False
    except Exception as e:
        print(f"FAILED Test 3 with error: {e}")
        all_passed = False

    # -------------------------------------------------------------
    # Summary
    # -------------------------------------------------------------
    print("---")
    if all_passed:
        print("ALL TESTS PASSED! 🎉\n")
    else:
        print("SOME TESTS FAILED! ❌\n")

if __name__ == "__main__":
    run_tests(insert_bits)