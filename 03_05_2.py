def sort_stack(input_stack:list[int]) -> list[int]:
    if input_stack is None: return None
    if not input_stack: return []
    # create a temporary stack, 
    temp = []
    result = []

    # result is with elements in increasing order from top to bottom (just as the solution requires us to do), 
    # So, at end we don't need to pop from this and put in input_stack
    #  smallest element sits at the top, biggest element lies at the bottom 
    # for the ones that fall somewhere in between, we pop from result stack until a larger element is found, then add current element and followed by putting all elements from temporarily stored stack

    while input_stack:
        curr = input_stack.pop()
        while result and curr > result[-1]:
            temp.append(result.pop())

        result.append(curr)
        while temp:
            result.append(temp.pop())

    # # put contents of result into input_stack
    # while result:
    #     input_stack.append(result.pop())

    return result

def run_sort_stack_tests():
    test_cases = [
        [],
        [5],
        [3, 1, 4, 2],
        [1, 2, 3, 4, 5],  # Already sorted
        [5, 4, 3, 2, 1],  # Reverse sorted
        [3, 3, 1, 2, 1],  # Duplicates
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 3.5: SORT STACK TESTS")
    print("=" * 60)

    for i, initial in enumerate(test_cases, 1):
        stack_input = list(initial)
        try:
            res_stack = sort_stack(stack_input)
            actual_stack = stack_input if res_stack is None else res_stack

            # Smallest item on top -> Popping items sequentially gives sorted ascending order
            popped = []
            temp = list(actual_stack)
            while temp:
                popped.append(temp.pop())

            assert popped == sorted(
                initial
            ), f"Stack not correctly sorted with smallest on top!\nExpected popped order: {sorted(initial)}\nGot: {popped}"
            print(f"  [PASS] Test {i:02d}: Initial {initial} -> Sorted Correctly")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"3.5 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_sort_stack_tests()