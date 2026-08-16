from typing import List

class Listy:
    def __init__(self, arr: List[int]):
        self._arr = list(arr)

    def element_at(self, index: int) -> int:
        if 0 <= index < len(self._arr):
            return self._arr[index]
        return -1

def search_listy(listy: Listy, target: int) -> int:
    if listy.element_at(0) is -1:
        return -1
    length = get_length_listy(listy)

    if target > listy.element_at(length - 1):
        return -1
    def binary_search_helper(left: int, right: int) -> int:
        if left > right:
            return -1
        mid = left + (right - left ) // 2

        if target == listy.element_at(mid):
            return mid
        elif target < listy.element_at(mid):
            return binary_search_helper(left, mid - 1)
        else:
            return binary_search_helper(mid + 1, right)

    return binary_search_helper(0, length - 1)

def get_length_listy(listy: Listy) -> int:
    check = 1
    while check >= 0:
        if listy.element_at(check) == -1:
            while check >= 0:
                if listy.element_at(check) != -1:
                    break
                check -= 1
            break
        check *= 2

    return (check + 1)

def run_search_listy_tests():
    test_cases = [
        ([], 5, -1, "Empty Listy"),
        ([10], 10, 0, "Single element match"),
        ([1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21], 1, 0, "First element search"),
        (
            [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],
            21,
            10,
            "Last element search",
        ),
        (
            [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],
            11,
            5,
            "Middle element search",
        ),
        (
            [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],
            8,
            -1,
            "Missing element in range",
        ),
        (
            [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21],
            100,
            -1,
            "Missing element far beyond bounds",
        ),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 10.4: SORTED SEARCH NO SIZE (LISTY) TESTS")
    print("=" * 60)

    for i, (raw_arr, target, expected_idx, desc) in enumerate(test_cases, 1):
        listy = Listy(raw_arr)
        try:
            res_idx = search_listy(listy, target)

            if expected_idx == -1:
                assert (
                    res_idx == -1
                ), f"Expected -1 for missing target {target}, got {res_idx}"
            else:
                assert res_idx != -1 and listy.element_at(res_idx) == target, (
                    f"Expected index with value {target}, got index {res_idx}"
                    f" (val={listy.element_at(res_idx)})"
                )

            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"10.4 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_search_listy_tests()