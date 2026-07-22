# LOGIC
# implement stack with array, for O(1) lookup, 
# update min_element with each pop and push operation,
# that too only when element less than min is pushed, and min_element is popped

# CODE
class MinStack:
    def __init__(self):
        # dynamic size array, so using size to access top element
        self.array = []
        # self.stack_size = 0
        self.min_element = float("inf")

    def is_empty(self):
        return len(self.array) == 0

    # def _top_index(self) -> int:
    #     return self.stack_size - 1
    
    def get_min(self) -> int:
        if self.is_empty():
            raise Exception(f"Stack is Empty.")
        # top_idx = self._top_index()
        return self.array[-1][1]

    def push(self, val):
        if self.is_empty():
            current_min = val
        else:
            # if pushed val is less than min, update min
            current_min = val if val < self.get_min() else self.get_min()
        # self.stack_size += 1
        self.array.append((val, current_min))
        return 

    def pop(self) -> int:
        if self.is_empty():
            raise Exception(f"Stack is Empty.")
        # top_idx = self._top_index()
        top_index_tuple = self.array.pop()
        top_element = top_index_tuple[0]
        # self.stack_size -= 1
        return top_element

    def peek(self) -> min:
        if self.is_empty():
            raise Exception(f"Stack is Empty.")
        top_element = self.array[-1][0]
        return top_element
    
    # =====================================================================
# PART 2: UNIVERSAL TEST TEMPLATE (DO NOT EDIT)
# =====================================================================

def run_tests(MinStackClass):
    print(f"Running Universal Test Suite for {MinStackClass.__name__}:\n")
    all_passed = True

    # -------------------------------------------------------------
    # Test 1: Empty State & Underflow Handling
    # -------------------------------------------------------------
    try:
        stack = MinStackClass()
        try:
            stack.get_min()
            print("FAILED Test 1: get_min() on empty stack did not raise Exception/Error.")
            all_passed = False
        except Exception:
            print("Passed Test 1: Empty state handled correctly.")
    except Exception as e:
        print(f"FAILED Test 1 with unexpected error: {e}")
        all_passed = False

    # -------------------------------------------------------------
    # Test 2: Standard LIFO Behavior & Min Tracking
    # -------------------------------------------------------------
    try:
        stack = MinStackClass()
        stack.push(5)
        check1 = (stack.get_min() == 5)
        
        stack.push(6)
        check2 = (stack.get_min() == 5) # Min should still be 5
        
        stack.push(3)
        check3 = (stack.get_min() == 3) # Min updates to 3
        
        stack.push(7)
        check4 = (stack.get_min() == 3) # Min should still be 3

        stack.pop() # Removes 7
        check5 = (stack.get_min() == 3) # Min is still 3
        
        stack.pop() # Removes 3
        check6 = (stack.get_min() == 5) # Min reverts back to 5

        if all([check1, check2, check3, check4, check5, check6]):
            print("Passed Test 2: Standard LIFO ordering and accurate Min tracking.")
        else:
            print("FAILED Test 2: Min value did not update correctly during normal push/pop.")
            all_passed = False
    except Exception as e:
        print(f"FAILED Test 2 with error: {e}")
        all_passed = False

    # -------------------------------------------------------------
    # Test 3: The "Duplicate Minimum" Edge Case
    # -------------------------------------------------------------
    try:
        stack = MinStackClass()
        stack.push(2)
        stack.push(1)
        stack.push(1) # Pushing a duplicate of the current minimum

        check1 = (stack.get_min() == 1)
        
        stack.pop() # Removes the top '1'
        check2 = (stack.get_min() == 1) # Min MUST still be 1 (because of the other '1')
        
        stack.pop() # Removes the second '1'
        check3 = (stack.get_min() == 2) # Min reverts to 2

        if check1 and check2 and check3:
            print("Passed Test 3: Duplicate minimum values handled flawlessly.")
        else:
            print("FAILED Test 3: Duplicate minimums corrupted the tracking logic.")
            all_passed = False
    except Exception as e:
        print(f"FAILED Test 3 with error: {e}")
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
    run_tests(MinStack)