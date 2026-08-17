# 1 GB available
# 8 billion bytes available for 4 billion non-negative numbers(almost 2x the number of non-negative integers), rest fall in long category, so input_file has duplicate values

from typing import List

def find_missing_int(stream: List[int], max_val: int = 100000) -> int:
    """CTCI 10.7: Finds an integer in range [0, max_val] that is NOT present in stream."""
    # strategy bit vector, initialised with 0s
    num_bytes = (max_val // 8) + 1
    bit_vector = bytearray(num_bytes) # bit vector initialised with 0s

    # scan the whole file, if number present set bit at index = number to 1
    # else let it stay 0
    for num in stream:
        # set bit at index num to 1
        if 0 <= num <= max_val:
            byte_idx = num // 8 # box number
            bit_idx = num % 8 # switch number
            # set bit with bitwise OR
            bit_vector[byte_idx] |= (1 << bit_idx)
            
    # start from beginning, first bit that is set to 0, is missing
    for byte_idx in range(num_bytes):
        for bit_idx in range(8):
            if bit_vector[byte_idx] & (1 << bit_idx) == 0 and byte_idx * 8 + bit_idx <= max_val:
                return byte_idx * 8 + bit_idx
            
    return None

def run_missing_int_tests():
    test_cases = [
        (list(range(1, 100)), 100, 0, "Missing first integer (0)"),
        (list(range(0, 99)), 100, 99, "Missing boundary integer (99)"),
        ([i for i in range(50) if i != 27], 50, 27, "Missing middle integer (27)"),
        ([], 10, None, "Empty stream input (Any int in [0, 10] is valid)"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 10.7: MISSING INT TESTS")
    print("=" * 60)

    for i, (stream, max_val, expected_missing, desc) in enumerate(test_cases, 1):
        try:
            res = find_missing_int(stream, max_val)
            assert isinstance(res, int), f"Result must be integer, got {type(res)}"
            assert 0 <= res <= max_val, f"Returned int {res} out of bounds [0, {max_val}]"
            assert res not in set(stream), f"Returned int {res} was actually present in stream"

            if expected_missing is not None:
                assert res == expected_missing, f"Expected missing {expected_missing}, got {res}"

            print(f"  [PASS] Test {i:02d}: {desc} (Returned: {res})")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(f"10.7 SUMMARY: {passed} PASSED | {failed} FAILED | Total: {len(test_cases)}")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_missing_int_tests()