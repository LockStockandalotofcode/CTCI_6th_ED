def draw_line(screen: bytearray, width:int, x1: int, x2: int, y: int) -> bytearray:
    """CTCI 5.8: Draws a horizontal line from (x1, y) to (x2, y) on a monochrome screen.

    'width' is in bits and is a multiple of 8. Screen is represented as a bytearray.
    """
    bytes_per_row = width // 8
    start_byte = x1 // 8
    end_byte = x2 // 8

    # in each byte, there's bits indexed 7, 6, 5, ... 0; reverse order
    # eg 3 to 26, 
    start_offset = x1 % 8
    end_offset = (x2 % 8)

    first_full_byte = start_byte if start_offset == 0 else start_byte + 1
    last_full_byte = end_byte if end_offset == 7 else end_byte - 1

    row_start = y * bytes_per_row

    # SET MASKS
    for b in range(first_full_byte, last_full_byte + 1):
        screen[row_start + b] = 0xFF # setting a single mask for entire middle full bytes between x1, and x2

    # partial masks, for partial bits
    # start mask is all 1s from start offset until end of byte (7)
    start_mask = 0xFF >> start_offset
    end_mask = (0xFF << (7 - end_offset)) & 0xFF

    if start_byte == end_byte:
        screen[row_start + start_byte] |= start_mask & end_mask
    else:
        screen[row_start + start_byte] |= start_mask
        screen[row_start + end_byte] |= end_mask

    return screen

def run_draw_line_tests():
    def ref_draw_line(
        screen: bytearray, width: int, x1: int, x2: int, y: int
    ) -> bytearray:
        res = bytearray(screen)
        bytes_per_row = width // 8
        for x in range(x1, x2 + 1):
            byte_idx = y * bytes_per_row + (x // 8)
            bit_offset = 7 - (x % 8)
            res[byte_idx] |= 1 << bit_offset
        return res

    test_cases = [
        (32, 2, 2, 5, 0, "Same byte partial line (x1=2, x2=5)"),
        (32, 2, 0, 7, 0, "Full single byte line (x1=0, x2=7)"),
        (32, 2, 3, 3, 1, "Single pixel line (x1=3, x2=3)"),
        (32, 2, 3, 22, 1, "Multi-byte line across boundaries (x1=3, x2=22)"),
        (32, 2, 0, 31, 0, "Full row width line (x1=0, x2=31)"),
        (64, 4, 8, 23, 2, "Exact byte alignment line (x1=8, x2=23)"),
        (16, 2, 0, 0, 0, "Boundary pixel at origin (x1=0, x2=0)"),
    ]

    passed, failed = 0, 0
    print("\n" + "=" * 60)
    print("RUNNING CTCI 5.8: DRAW LINE TESTS")
    print("=" * 60)

    for i, (width, height, x1, x2, y, desc) in enumerate(test_cases, 1):
        try:
            screen_size = (width // 8) * height
            initial_screen = bytearray(screen_size)

            expected = ref_draw_line(initial_screen, width, x1, x2, y)

            # Test function
            actual = draw_line(bytearray(initial_screen), width, x1, x2, y)

            assert actual is not None, "Function returned None instead of bytearray"
            assert list(actual) == list(expected), (
                f"Mismatch for width={width}, x1={x1}, x2={x2}, y={y}.\n"
                f"Expected: {[hex(b) for b in expected]}\n"
                f"Got:      {[hex(b) for b in actual]}"
            )

            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"5.8 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_draw_line_tests()