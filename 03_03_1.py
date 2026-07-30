
# implementing a single stack from scratch
class SetOfStacks:
    def __init__(self, capacity: int):
        self.list_stacks = []
        self.curr_stack = []
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
        return

    def _update_to_prev_stack(self):
        self.list_stacks.pop(-1)
        #  if list of stacks is empty, we create new empty curr_stack
        #  else we move it to previous stack, one-index-before current stack
        if self.is_empty_list_of_stacks():
            self.curr_stack = []
            self.list_stacks.append(self.curr_stack)
        else:
            self.curr_stack = self.list_stacks[-1]
            
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

if __name__ == "__main__":
    run_set_of_stacks_tests()