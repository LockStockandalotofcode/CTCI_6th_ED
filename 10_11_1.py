from typing import List

def max_index(arr: List[int], a: int, b: int, c: int) -> int:
    # out of bound checking for indices is done here itself
    n = len(arr)
    a_val = arr[a] if 0 <= a < n else float("-inf")
    b_val = arr[b] if 0 <= b < n else float("-inf")
    c_val = arr[c] if 0 <= c < n else float("-inf")
    max_val = max(a_val, b_val, c_val)

    if max_val == a_val:
        return a
    elif max_val == b_val:
        return b
    else:
        return c

def sort_valley_peak(arr: List[int]) -> List[int]:
    """CTCI 10.11: Rearranges array into alternating sequence of peaks and valleys."""
    # need to go through only even indices (0, 2, 4, ...)
    for i in range(0, len(arr), 2):
        max_idx = max_index(arr, i-1, i, i+1)
        if i != max_idx:
            # swap
            arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

def run_peaks_and_valleys_tests():
    def validate_peaks_and_valleys(arr: List[int]) -> bool:
        if len(arr) <= 2:
            return True
        for i in range(1, len(arr) - 1):
            is_peak = arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]
            is_valley = arr[i] <= arr[i - 1] and arr[i] <= arr[i + 1]
            if not (is_peak or is_valley):
                return False
        return True

    test_cases = [
        ([], "Empty array"),
        ([5], "Single element"),
        ([5, 3], "Two elements"),
        ([5, 3, 1, 2, 3], "CTCI example array [5, 3, 1, 2, 3]"),
        ([1, 2, 3, 4, 5, 6], "Sorted array input"),
        ([2, 2, 2, 2], "Array with identical values"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 10.11: PEAKS AND VALLEYS TESTS")
    print("=" * 60)

    for i, (arr, desc) in enumerate(test_cases, 1):
        try:
            res = sort_valley_peak(arr.copy())
            assert len(res) == len(
                arr
            ), f"Length changed from {len(arr)} to {len(res)}"
            assert sorted(res) == sorted(
                arr
            ), "Output contains different element multiset"
            assert validate_peaks_and_valleys(
                res
            ), f"Array {res} fails alternating peak/valley condition"

            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"10.11 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_peaks_and_valleys_tests()