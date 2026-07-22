#logic
class MyQueue:
    def __init__(self):
        self.push_stack = [] #s1
        self.pop_stack = [] #s2
    
    def is_empty(self) -> bool:
        return (len(self.push_stack) == 0 and len(self.pop_stack) == 0)

    def enqueue(self, val):
        if len(self.push_stack) == 0 and len(self.pop_stack) != 0:
            self.transfer_to_s1()
        # now push
        self.push_stack.append(val)
        return

    def transfer_to_s1(self):
        for _ in range(len(self.pop_stack)):
            element = self.pop_stack.pop()
            self.push_stack.append(element)
        return

    def transfer_to_s2(self):
        for _ in range(len(self.push_stack)):
            element = self.push_stack.pop()
            self.pop_stack.append(element)
        return 
    
    def dequeue(self):
        if self.is_empty():
            raise Exception(f"Queue is Empty.")
        if len(self.push_stack) != 0 and len(self.pop_stack) == 0:
            self.transfer_to_s2()
        
        return self.pop_stack.pop()

    def peek(self):
        if self.is_empty():
            raise Exception(f"Queue is Empty.")
        if len(self.push_stack) != 0 and len(self.pop_stack) == 0:
            self.transfer_to_s2()
        
        return self.pop_stack[-1]

# TESTING
# =====================================================================
# PART 2: UNIVERSAL TEST TEMPLATE (DO NOT EDIT)
# =====================================================================

def run_tests(QueueClass):
    print(f"Running Universal Test Suite for {QueueClass.__name__}:\n")
    all_passed = True

    # -------------------------------------------------------------
    # Test 1: Empty State & Underflow Handling
    # -------------------------------------------------------------
    try:
        q = QueueClass()
        try:
            q.dequeue()
            print("FAILED Test 1: dequeue() on empty queue did not raise Exception/Error.")
            all_passed = False
        except Exception:
            pass # Expected behavior
            
        try:
            q.peek()
            print("FAILED Test 1: peek() on empty queue did not raise Exception/Error.")
            all_passed = False
        except Exception:
            print("Passed Test 1: Empty state handled correctly.")
    except Exception as e:
        print(f"FAILED Test 1 with unexpected error: {e}")
        all_passed = False

    # -------------------------------------------------------------
    # Test 2: Standard FIFO Behavior (Bulk load, bulk unload)
    # -------------------------------------------------------------
    try:
        q = QueueClass()
        q.enqueue(10)
        q.enqueue(20)
        q.enqueue(30)
        
        check1 = (q.peek() == 10)
        check2 = (q.dequeue() == 10)
        check3 = (q.dequeue() == 20)
        check4 = (q.dequeue() == 30)
        check5 = q.is_empty()

        if all([check1, check2, check3, check4, check5]):
            print("Passed Test 2: Standard FIFO ordering works perfectly.")
        else:
            print("FAILED Test 2: Elements did not dequeue in correct FIFO order.")
            all_passed = False
    except Exception as e:
        print(f"FAILED Test 2 with error: {e}")
        all_passed = False

    # -------------------------------------------------------------
    # Test 3: The "Interleaved Operations" Edge Case
    # -------------------------------------------------------------
    try:
        q = QueueClass()
        q.enqueue(1)
        q.enqueue(2)
        
        # Dequeue one item (Should be 1). This forces the stacks to shift.
        check1 = (q.dequeue() == 1)
        
        # Enqueue more items WHILE the second stack already has elements
        q.enqueue(3)
        q.enqueue(4)
        
        # Dequeue the rest. If shifting logic is wrong, this will return 3 instead of 2.
        check2 = (q.dequeue() == 2)
        check3 = (q.dequeue() == 3)
        check4 = (q.dequeue() == 4)

        if all([check1, check2, check3, check4]):
            print("Passed Test 3: Interleaved enqueue/dequeue states handled flawlessly.")
        else:
            print("FAILED Test 3: State corrupted during mixed push/pop operations. Check your stack shifting logic.")
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
    run_tests(MyQueue)