# recursion logic
# power set {a, b, c} = power set {a, b} + (union of all elements in power set of {a, b} + {c})

# Bottom-up approach
def power_set(nums: list) -> list[list]:
    # if nums is None: return []
    if not nums: return [[]]

    # starting with empty subset
    result = [[]]

    for num in nums:
        new_additions_list = []
        for subset in result:
            new_addition = subset + [num]
            new_additions_list.append(new_addition)
        result.extend(new_additions_list)
    return result

def run_power_set_tests():
    test_cases = [
        [],
        [1],
        [1, 2],
        [1, 2, 3],
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 8.4: POWER SET TESTS")
    print("=" * 60)

    for i, nums in enumerate(test_cases, 1):
        try:
            res = power_set(nums)

            # Convert result into set of frozensets to compare independent of order
            res_set = {frozenset(s) for s in res}

            # Mathematical validation: 2^N subsets
            assert len(res) == (
                1 << len(nums)
            ), f"Expected {1 << len(nums)} subsets, got {len(res)}"
            assert len(res_set) == (
                1 << len(nums)
            ), "Duplicate subsets detected in output!"

            print(
                f"  [PASS] Test {i:02d}: N={len(nums)} -> Generated"
                f" {len(res)} Unique Subsets"
            )
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: N={len(nums)} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"8.4 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_power_set_tests()