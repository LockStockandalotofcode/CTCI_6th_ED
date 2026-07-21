# PROBLEM 02_03

# # # LOGIC

# ERRORS IN MY LOGIC
# NOT NECESSARILY CIRCULAR LINKED LIST, SO NO WAY TO MOVE FROM TAIL TO HEAD NODE, 

# 2 pointers: slow moves 1, fast moves 2; when slow reaches tail node, fast is the node prev to middle node
# thenremove the node

# # assumptions clarifications
# singly linked list given
# considering 2nd middle node as middle node in even length list

# # TEST_CASES
# test_cases = (
#     # normal case 
#     # even, odd len
#     # empty case
#     # edge case- single len linked list
# )
# CODE

# implement LinkedList Class
# implementation : Linked List made up of LinkedListNode
class LinkedListNode:
    def __init__(self, val, next_val=None, prev_val=None):
        self.val = val
        self.next = next_val

        # if doubly linked, include below line
        # self.prev = prev_val

class LinkedList:
    # keeping head node, tail node, endmost nodes for easier testing
    def __init__(self, values=None):
        self.head = None
        self.tail = None
        if values is not None:
            self.add_values(values)
    
    def add(self, value):
        if self.head is None:
            self.head = self.tail = LinkedListNode(val=value)
        else:
            self.tail.next = LinkedListNode(value)
            self.tail = self.tail.next
        return self.tail
            
    def add_values(self, values):
        for v in values:
            self.add(v)
    
    def values(self) -> list:
        # traverse linked list and append values to a result list
        res = []
        curr_node = self.head
        while curr_node:
            res.append(curr_node.val)
            curr_node = curr_node.next
        
        return res
    
def delete_mid(mid_node: LinkedListNode) -> None:
	if not mid_node:
		return 
	
	slow = fast = mid_node
	while slow:
		slow = slow.next
		if fast.next is None or fast.next.next is None:
			fast = head.next # but we dont have access to head node
		else:
			fast = fast.next.next
	
	prev_node = fast
	# remove mid node
	prev_node.next = mid_node.next
	return
	
    
# # testing 
# print("Running test cases: ")
# all_passed = True

# for idx, (input_values, exp_output) in enumerate(test_cases, 1):
#     linked_list = LinkedList(input_values)
#     result_linked_list = delete_mid(linked_list)
#     result = result_linked_list.values()
#     if result == exp_output:
#         print(f"passed Test {idx}.")
#     else:
#         print(f"failed Test {idx} - Input: {input_values} | Expected: {exp_output} | Got: {result}")
#         all_passed = False

# if all_passed == True:
#     print("\n All cases PASSED.")