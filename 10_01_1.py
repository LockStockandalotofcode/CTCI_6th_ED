import copy

def sorted_merge(a: list[int], b: list[int], count_a: int, count_b: int):
#     Merges sorted array b into sorted array a in-place.

#     count_a is the number of valid elements in a.
#     count_b is the number of valid elements in b.
#     len(a) == count_a + count_b.

    # absolute base case
    if count_a == 0:
        return b
    if count_b == 0:
        return a

    res = [0] * (count_a + count_b)
    ptr_res = 0

    if b[0] > a[count_a - 1]:
        res[: count_a] = a[: count_a]
        res[count_a: ] = b
        return res

    if b[-1] < a[0]:
        res[: count_b] = b
        res[count_b: ] = a[ : count_a]
        return res
    
    ptr_a, ptr_b = 0, 0

    while ptr_a < count_a and ptr_b < count_b:
        if a[ptr_a] <= b[ptr_b]:
            res[ptr_res] = a[ptr_a]; ptr_res += 1

            if (ptr_a + 1) < count_a:
                if b[ptr_b] <= a[ptr_a + 1]:
                    res[ptr_res] = b[ptr_b]; ptr_res += 1
                    ptr_b += 1
                elif b[ptr_b] > a[ptr_a + 1]:
                # else:
                    res[ptr_res] = a[ptr_a + 1]; ptr_res += 1
                    ptr_a += 1
                
            ptr_a += 1

        else:
            res[ptr_res] = b[ptr_b]; ptr_res += 1
            ptr_b += 1

    if ptr_a < count_a:
        res[ptr_res: ] = a[ptr_a : count_a]
    if ptr_b < count_b:
        res[ptr_res: ] = b[ptr_b : ]

    return res

def check_algorithm(fn):
    passed = 0
    failed = 0

    test_cases = [
        # (a, b, count_a, count_b, expected)
        ([], [], 0, 0, []),
        ([1, 2, 3], [], 3, 0, [1, 2, 3]),
        ([0, 0, 0], [1, 2, 3], 0, 3, [1, 2, 3]),
        ([2, 0], [1], 1, 1, [1, 2]),
        ([1, 0], [2], 1, 1, [1, 2]),
        ([1, 3, 5, 0, 0, 0], [2, 4, 6], 3, 3, [1, 2, 3, 4, 5, 6]),
        ([10, 20, 30, 0, 0], [15, 25], 3, 2, [10, 15, 20, 25, 30]),
        ([10, 20, 30, 0, 0], [1, 2], 3, 2, [1, 2, 10, 20, 30]),
        ([1, 2, 0, 0, 0], [10, 20, 30], 2, 3, [1, 2, 10, 20, 30]),
        ([2, 2, 2, 0, 0, 0], [2, 2, 2], 3, 3, [2, 2, 2, 2, 2, 2]),
        ([1, 3, 3, 0, 0], [2, 3], 3, 2, [1, 2, 3, 3, 3]),
        ([-5, -1, 0, 0, 0], [-10, 2], 2, 2, [-10, -5, -1, 2]),
        ([-3, 0, 5, 0, 0], [-2, 0], 3, 2, [-3, -2, 0, 0, 5]),
    ]
    
    print("=" * 60)
    print("RUNNING OUT-OF-PLACE MERGE TESTS")
    print("=" * 60)

    for i, (*args, expected) in enumerate(test_cases, 1):
        try:
            # Unpack the 4 function arguments: a, b, count_a, count_b
            result = fn(*args)
            assert result == expected, f"Expected {expected}, got {result}"
            print(f"  [PASS] Test {i:02d}: Output = {result}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: ERROR -> {e}")
            failed += 1

    print("-" * 60)
    print(f"SUMMARY: {passed} PASSED | {failed} FAILED | Total: {len(test_cases)}")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    check_algorithm(sorted_merge)