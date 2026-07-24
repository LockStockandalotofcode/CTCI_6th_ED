import copy

def sorted_merge(a: list[int], b: list[int], count_a: int, count_b: int) -> None:
#     Merges sorted array b into sorted array a in-place.

#     count_a is the number of valid elements in a.
#     count_b is the number of valid elements in b.
#     len(a) == count_a + count_b.

    # absolute base case
    if not b:
        return a

    if count_a == 0:
        return b
    if b[0] > a[-1]:
        return a + b
    res = [0] * (count_a + count_b)
    ptr_res = 0

    ptr_a, ptr_b = 0, 0
    while ptr_a < count_a or ptr_b < count_b:
        # if b's element fits in
        if a[ptr_a] <= b[ptr_b] < a[ptr_a + 1]:
            # insert b's element in res
            res[ptr_res] = b[ptr_b]
            ptr_b += 1
            ptr_a += 1
        # otherwise, increment ptr_a
        else:
            res[ptr_res] = a[ptr_a]
            ptr_a += 1

        ptr_res += 1

    a = res
    return 

def run_sorted_merge_tests():
    test_cases = [
        # (a_initial, b, count_a, count_b, expected)
        # 1. Empty / Zero Cases
        ([], [], 0, 0, []),
        ([1, 2, 3], [], 3, 0, [1, 2, 3]),  # B is empty
        (
            [0, 0, 0],
            [1, 2, 3],
            0,
            3,
            [1, 2, 3],
        ),  # A has no initial elements (buffer only)
        # 2. Single Element Cases
        ([2, 0], [1], 1, 1, [1, 2]),  # B element smaller
        ([1, 0], [2], 1, 1, [1, 2]),  # A element smaller
        # 3. Interleaved Normal Cases
        (
            [1, 3, 5, 0, 0, 0],
            [2, 4, 6],
            3,
            3,
            [1, 2, 3, 4, 5, 6],
        ),
        (
            [10, 20, 30, 0, 0],
            [15, 25],
            3,
            2,
            [10, 15, 20, 25, 30],
        ),
        # 4. Disjoint Ranges (Subtle Edge Cases)
        (
            [10, 20, 30, 0, 0],
            [1, 2],
            3,
            2,
            [1, 2, 10, 20, 30],
        ),  # All B smaller than A
        (
            [1, 2, 0, 0, 0],
            [10, 20, 30],
            2,
            3,
            [1, 2, 10, 20, 30],
        ),  # All B larger than A
        # 5. Duplicates & Identical Values
        (
            [2, 2, 2, 0, 0, 0],
            [2, 2, 2],
            3,
            3,
            [2, 2, 2, 2, 2, 2],
        ),
        (
            [1, 3, 3, 0, 0],
            [2, 3],
            3,
            2,
            [1, 2, 3, 3, 3],
        ),
        # 6. Negative Numbers & Zeroes
        (
            [-5, -1, 0, 0, 0],
            [-10, 2],
            2,
            2,
            [-10, -5, -1, 2],
        ),
        (
            [-3, 0, 5, 0, 0],
            [-2, 0],
            3,
            2,
            [-3, -2, 0, 0, 5],
        ),
    ]

    passed = 0
    failed = 0
    print("=" * 60)
    print("RUNNING CTCI 10.1: SORTED MERGE TESTS")
    print("=" * 60)

    for i, (a_initial, b, count_a, count_b, expected) in enumerate(
        test_cases, 1
    ):
        a = copy.deepcopy(a_initial)
        b_copy = copy.deepcopy(b)
        try:
            sorted_merge(a, b_copy, count_a, count_b)
            assert (
                a == expected
            ), f"Array A mismatch!\nExpected: {expected}\nGot:      {a}"
            print(f"  [PASS] Test {i:02d}: a = {a_initial}, b = {b}")
            passed += 1
        except Exception as e:
            print(
                f"  [FAIL] Test {i:02d}: a = {a_initial}, b = {b} -> ERROR:"
                f" {e}"
            )
            failed += 1

    print("-" * 60)
    print(
        f"10.1 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_sorted_merge_tests()