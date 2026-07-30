
# implementing a single stack from scratch
class SetOfStacks:
    def __init__(self, capacity: int):
        self.list_stacks = []
        self.curr_stack = []
        self.curr_stack_idx = 0
        self.list_stacks.append(self.curr_stack)
        self.capacity = capacity

    def push(self, val: int) -> None:
        # if stack exceeds capacity, we move to next stack
        if len(self.curr_stack) == self.capacity:
            self._create_new_next_stack()
        self.curr_stack.append(val)
        return
    
    def _get_top(self):
        return self.curr_stack[-1]
    
    def pop(self) -> int:
        top_element = self._get_top()
        # remove the top element
        self.curr_stack.pop(-1)
        # if this makes the curr_stack empty, we should move to the stack previous to it list_stacks
        if self.is_empty_stack():
            self._update_to_prev_stack()
        
        return top_element
    
    def popAt(self, index: int) -> int | None:
        # base case
        if index < 0 or index >= len(self.list_stacks): raise IndexError
        
        self.curr_stack = self.list_stacks[index]
        top_element = self._get_top()
        # remove the top element
        self.curr_stack.pop(-1)
        # if this makes the curr_stack empty, we should move to the stack previous to it list_stacks
        if self.is_empty_stack():
            self._update_to_prev_stack()

        # set curr_stack to last stack in the list_of_stacks
        self.curr_stack_idx = len(self.list_stacks) - 1
        self.curr_stack = self.list_stacks[self.curr_stack_idx]
        
        return top_element

    def peek(self):
        top_element = self._get_top()
        return top_element

    def is_empty_list_of_stacks(self) -> bool:
        for stack in self.list_stacks:
            if len(stack) != 0: return False

        return True

    def is_empty_stack(self) -> bool:
        return True if len(self.curr_stack) == 0 else False

    def _create_new_next_stack(self):
        new_stack = []
        self.list_stacks.append(new_stack)
        self.curr_stack = self.list_stacks[-1]
        self.curr_stack_idx += 1
        return

    def _update_to_prev_stack(self):
        self.list_stacks.pop(-1)
        #  if list of stacks is empty, we create new empty curr_stack
        #  else we move it to previous stack, one-index-before current stack
        if self.is_empty_list_of_stacks():
            self.curr_stack = []
            self.list_stacks.append(self.curr_stack)
            self.curr_stack_idx = 0
        else:
            self.curr_stack = self.list_stacks[-1]
            self.curr_stack_idx -= 1
            
        return

def run_set_of_stacks_tests():
    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 3.3: SET OF STACKS TESTS")
    print("=" * 60)

    # Test 1: Standard Push/Pop within Capacity
    try:
        sos = SetOfStacks(capacity=2)
        sos.push(10)
        sos.push(20)
        assert sos.pop() == 20
        assert sos.pop() == 10
        print("  [PASS] Test 01: Basic Single Stack Capacity Push/Pop")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 01 -> ERROR: {e}")
        failed += 1

    # Test 2: Sub-stack Rollover across Multiple Stacks
    try:
        sos = SetOfStacks(capacity=2)
        elements = [1, 2, 3, 4, 5]  # Spans 3 sub-stacks (size 2, 2, 1)
        for elem in elements:
            sos.push(elem)

        popped = []
        for _ in range(len(elements)):
            popped.append(sos.pop())

        assert (
            popped == elements[::-1]
        ), f"LIFO order broken across sub-stacks! Expected {elements[::-1]}, got {popped}"
        print(
            "  [PASS] Test 02: Multi-Stack Rollover LIFO Verification"
            " (Push 5 items, capacity 2)"
        )
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 02 -> ERROR: {e}")
        failed += 1

    # Test 3: Large Volume Interleaved Operations
    try:
        sos = SetOfStacks(capacity=3)
        for i in range(100):
            sos.push(i)

        for i in range(99, -1, -1):
            val = sos.pop()
            assert (
                val == i
            ), f"Popped wrong value during large volume drain. Expected {i}, got {val}"

        print("  [PASS] Test 03: 100-Element Rollover Stress Test")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 03 -> ERROR: {e}")
        failed += 1

    print("-" * 60)
    print(f"3.3 SUMMARY: {passed} PASSED | {failed} FAILED | Total: 3")
    print("=" * 60 + "\n")

def run_set_of_stacks_followup_tests():
    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 3.3 FOLLOW-UP: popAt(index) TESTS")
    print("=" * 60)

    # Test 1: Direct popAt Target Verification
    try:
        sos = SetOfStacks(capacity=2)
        # Push 6 items across 3 sub-stacks:
        # Stack 0: [1, 2]
        # Stack 1: [3, 4]
        # Stack 2: [5, 6]
        for val in [1, 2, 3, 4, 5, 6]:
            sos.push(val)

        res_0 = sos.popAt(0)  # Top of Stack 0 -> 2
        res_1 = sos.popAt(1)  # Top of Stack 1 -> 4
        res_2 = sos.popAt(2)  # Top of Stack 2 -> 6

        assert res_0 == 2, f"popAt(0) failed! Expected 2, got {res_0}"
        assert res_1 == 4, f"popAt(1) failed! Expected 4, got {res_1}"
        assert res_2 == 6, f"popAt(2) failed! Expected 6, got {res_2}"

        print("  [PASS] Test 01: Direct Sub-stack Targeting via popAt")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 01 -> ERROR: {e}")
        failed += 1

    # Test 2: Out of Bounds Index Validation
    try:
        sos = SetOfStacks(capacity=2)
        sos.push(10)
        sos.push(20)

        # Only 1 sub-stack exists at index 0
        invalid_indices = [-1, 1, 5]
        for idx in invalid_indices:
            caught = False
            try:
                sos.popAt(idx)
            except IndexError:
                caught = True
            assert caught, f"Expected IndexError for popAt({idx}), but no exception was raised!"

        print("  [PASS] Test 02: Out of Bounds Index Validation")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 02 -> ERROR: {e}")
        failed += 1

    # Test 3: Interleaved pop() and popAt() State Integrity
    try:
        sos = SetOfStacks(capacity=3)
        # Push 6 items:
        # Stack 0: [10, 20, 30]
        # Stack 1: [40, 50, 60]
        for val in [10, 20, 30, 40, 50, 60]:
            sos.push(val)

        val1 = sos.popAt(0)  # Pops 30 from Stack 0
        assert val1 == 30, f"Expected 30 from popAt(0), got {val1}"

        val2 = sos.pop()      # Standard pop() should pop from top active stack (Stack 1) -> 60
        assert val2 == 60, f"Expected 60 from standard pop(), got {val2}"

        val3 = sos.pop()      # Standard pop() -> 50
        assert val3 == 50, f"Expected 50 from standard pop(), got {val3}"

        print("  [PASS] Test 03: Interleaved pop() and popAt() State Integrity")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 03 -> ERROR: {e}")
        failed += 1

    # Test 4: Draining a Sub-stack via popAt
    try:
        sos = SetOfStacks(capacity=2)
        # Stack 0: [1, 2]
        # Stack 1: [3, 4]
        for val in [1, 2, 3, 4]:
            sos.push(val)

        assert sos.popAt(1) == 4
        assert sos.popAt(1) == 3  # Stack 1 is now completely empty

        # Standard pop() should safely fall back to Stack 0 -> returns 2
        val_fallback = sos.pop()
        assert val_fallback == 2, f"Expected fallback pop() to return 2, got {val_fallback}"

        print("  [PASS] Test 04: Sub-stack Exhaustion & Fallback")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 04 -> ERROR: {e}")
        failed += 1

    print("-" * 60)
    print(f"3.3 FOLLOW-UP SUMMARY: {passed} PASSED | {failed} FAILED | Total: 4")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_set_of_stacks_tests()
    run_set_of_stacks_followup_tests()