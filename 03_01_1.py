# Approach 1: first Fixed size array allocation then populating the stack

class ThreeInOne:
    def __init__(self, stack_capacity=10):
        self.num_stacks = 3
        self.stack_capacity = stack_capacity

        # creating fixed size array of maz size possible
        self.arr = [None] * (self.stack_capacity * self.num_stacks)
        # tracking the current sizes of stacks - 0based indexing
        self.sizes = [0] * self.num_stacks

    def _top_index(self, stack_num):
        """Helper to get index of top element of a stack"""
        offset = (stack_num ) * self.stack_capacity
        size_of_Stack = self.sizes[stack_num] 
        return offset + (size_of_Stack - 1)
      
    def push(self, stack_num, val):
        # only when stack is not at full capacity
        if self.sizes[stack_num] >= self.stack_capacity:
            raise Exception(f"Stack {stack_num} at full capacity.")

        # increase stack capacity
        self.sizes[stack_num] += 1
        # push val to stack
        s_top_idx = self._top_index(stack_num)
        self.arr[s_top_idx] = val

    def pop(self, stack_num):
        # only when stack is not empty
        if self.sizes[stack_num] <= 0:
            raise Exception(f"Stack {stack_num} is Empty.")
        
        s_top_idx = self._top_index(stack_num)
        value = self.arr[s_top_idx]
        # pop val from stack
        self.arr[s_top_idx] = None
        # decrease stack capacity
        self.sizes[stack_num] -= 1
        return value

    def peek(self, stack_num):
        # only when stack is not empty
        if self.sizes[stack_num] <= 0:
            raise Exception(f"Stack {stack_num} is Empty.")
        
        s_top_idx = self._top_index(stack_num)
        value = self.arr[s_top_idx]
        return value

    def is_empty(self, stack_num) -> bool:
        if self.sizes[stack_num] == 0:
            return True
        return False

# =====================================================================
# UNIVERSAL TEST TEMPLATE 
# =====================================================================

def run_tests(ThreeInOneClass):
    """
    Pass your class definition as an argument to this function.
    Example: run_tests(MyThreeInOneImplementation)
    """
    print(f"Running Universal Test Suite for {ThreeInOneClass.__name__}:\n")
    all_passed = True

    # -------------------------------------------------------------
    # Test 1: Empty State & Underflow Handling
    # -------------------------------------------------------------
    try:
        stacks = ThreeInOneClass()
        # Verify initial state across all 3 stacks
        if not (stacks.is_empty(0) and stacks.is_empty(1) and stacks.is_empty(2)):
            print("FAILED Test 1: Stacks are not initially empty.")
            all_passed = False
        else:
            # Expect exception/error when popping from empty stack
            try:
                stacks.pop(0)
                print("FAILED Test 1: Popping from empty stack did not raise Exception.")
                all_passed = False
            except Exception:
                print("Passed Test 1: Empty state and underflow checks.")
    except Exception as e:
        print(f"FAILED Test 1 with unexpected error: {e}")
        all_passed = False

    # -------------------------------------------------------------
    # Test 2: Standard LIFO Behavior & Multi-Element Operations
    # -------------------------------------------------------------
    try:
        stacks = ThreeInOneClass()
        stacks.push(0, 100)
        stacks.push(0, 200)
        
        val_peek = stacks.peek(0)
        val_pop1 = stacks.pop(0)
        val_pop2 = stacks.pop(0)

        if val_peek == 200 and val_pop1 == 200 and val_pop2 == 100 and stacks.is_empty(0):
            print("Passed Test 2: Standard LIFO ordering (Push/Pop/Peek).")
        else:
            print("FAILED Test 2: LIFO ordering violated or values mismatched.")
            all_passed = False
    except Exception as e:
        print(f"FAILED Test 2 with error: {e}")
        all_passed = False

    # -------------------------------------------------------------
    # Test 3: Cross-Stack Isolation (No Crosstalk)
    # -------------------------------------------------------------
    try:
        stacks = ThreeInOneClass()
        # Push different elements into different stacks
        stacks.push(0, "S0_Value_1")
        stacks.push(1, "S1_Value_1")
        stacks.push(2, "S2_Value_1")

        stacks.push(1, "S1_Value_2")

        # Mutate Stack 1 and verify Stack 0 and Stack 2 remain completely untouched
        stacks.pop(1)

        check_0 = (stacks.peek(0) == "S0_Value_1")
        check_1 = (stacks.peek(1) == "S1_Value_1")
        check_2 = (stacks.peek(2) == "S2_Value_1")

        if check_0 and check_1 and check_2:
            print("Passed Test 3: Strict stack isolation (no memory leakage across stacks).")
        else:
            print("FAILED Test 3: Operations on one stack corrupted another.")
            all_passed = False
    except Exception as e:
        print(f"FAILED Test 3 with error: {e}")
        all_passed = False

    # -------------------------------------------------------------
    # Test 4: Heavy Load / Interleaved Interleaved Operations
    # -------------------------------------------------------------
    try:
        stacks = ThreeInOneClass()
        
        # Interleave pushes across all stacks
        for i in range(10):
            stacks.push(0, f"s0_{i}")
            stacks.push(1, f"s1_{i}")
            stacks.push(2, f"s2_{i}")

        # Pop from Stack 0 while leaving Stack 1 & 2 intact
        popped_s0 = [stacks.pop(0) for _ in range(10)]
        expected_s0 = [f"s0_{i}" for i in reversed(range(10))]

        # Verify Stack 1 and 2 top elements remain intact
        if popped_s0 == expected_s0 and stacks.peek(1) == "s1_9" and stacks.peek(2) == "s2_9":
            print("Passed Test 4: Heavy interleaved push/pop operations.")
        else:
            print("FAILED Test 4: Data corrupted under interleaved load.")
            all_passed = False
    except Exception as e:
        print(f"FAILED Test 4 with error: {e}")
        all_passed = False

    # -------------------------------------------------------------
    # Summary
    # -------------------------------------------------------------
    print("---")
    if all_passed:
        print("ALL TESTS PASSED! 🎉\n")
    else:
        print("SOME TESTS FAILED! ❌\n")

if __name__ == "__main__":
    run_tests(ThreeInOne)