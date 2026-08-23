from typing import List

def set_bit():
    pass 

def find_poisoned_bottle(
    total_bottles: int, strip_results: List[bool]
) -> int:
    """CTCI 6.10: Identifies the 1-based poisoned bottle ID given boolean results of 10 test strips.

    strip_results[i] is True if strip i turned positive.
    """
    # bit vector approach
    # each number (0 to 2 ** 10) uniquely represents all the numbers from 0 to 1000
    # since 1000 < 2 ** 10
    # each bit from 0 to 9(10 strips), tracks whether 

    # for every number add drop from this bottle onto strips that have a bit = 1
    # eg. 9 = 0b 1001
    # we add drop to strip 0 and 3 only, 
    # after 7 days, when we have results from strips, 
    # we construct the bottle index from the binary code from strips, by setting only those bits to 1
    
    poisoned_val = 0

    # reconstruct binary number from strip results
    for i, positive in enumerate(strip_results):
        if positive:
            poisoned_val = poisoned_val | (1 << i)

    # since its 0-based indexing, but bottles are 1-indexed
    return poisoned_val + 1

def run_poison_tests():
    def build_strip_results(poisoned_id: int, num_strips: int = 10) -> List[bool]:
        # Strip i tests bit i of (poisoned_id - 1) or poisoned_id depending on 0/1 indexing
        # Using standard binary encoding where strip i corresponds to bit i
        val = poisoned_id - 1
        return [bool((val >> i) & 1) for i in range(num_strips)]

    test_cases = [
        (1000, 1, "First bottle poisoned (ID 1)"),
        (1000, 2, "Second bottle poisoned (ID 2)"),
        (1000, 512, "Mid-range bottle poisoned (ID 512)"),
        (1000, 999, "Bottle 999 poisoned"),
        (1000, 1000, "Last bottle in 1000 set (ID 1000)"),
        (1024, 1024, "Max capacity bottle for 10 strips (2^10 = 1024)"),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 6.10: POISON TESTS")
    print("=" * 60)

    for i, (total, poisoned_id, desc) in enumerate(test_cases, 1):
        try:
            strip_results = build_strip_results(poisoned_id)

            res = find_poisoned_bottle(total, strip_results)

            # Accept both 1-based and 0-based results from user solver
            if res == poisoned_id - 1:
                res += 1

            assert res == poisoned_id, (
                f"For poisoned bottle {poisoned_id}: Expected {poisoned_id},"
                f" got {res}"
            )

            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"6.10 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_poison_tests()