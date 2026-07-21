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

test_cases = (
    # ([input_list], index_of_node_to_delete, [expected_output_list])
    # normal case 
    # even, odd len
    ([1, 2, 3, 4, 5], 2, [1, 2, 4, 5]),       # delete node at index 2 (val 3)
    (['a', 'b', 'c', 'd', 'e', 'f'], 3, ['a', 'b', 'c', 'e', 'f']), # delete node at index 1 (val 'b')
    (['c', 'd', 'e', 'f'], 2, ['c', 'd', 'f']), # delete node at index 1 (val 'b')
    # edge case- single len linked list
    ([2], 1, [2]),
    # empty case
    ([], 0, [])
)

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
    
def delete_mid(mid_node: LinkedListNode) -> bool:
    if not mid_node or not mid_node.next:
        return False
    # deleting next node after coping its data into given middle node
    mid_node.val = mid_node.next.val
    mid_node.next = mid_node.next.next

    return True
    
print("Running test cases: ")
all_passed = True

for idx, (input_vals, target_idx, exp_output) in enumerate(test_cases, 1):
    linked_list = LinkedList(input_vals)
    
    # Grab the target node to delete by traversing to target_idx
    curr = linked_list.head
    for _ in range(target_idx):
        curr = curr.next
    
    delete_mid(curr)
    
    result = linked_list.values()
    if result == exp_output:
        print(f"Passed Test {idx}.")
    else:
        print(f"Failed Test {idx} - Expected: {exp_output} | Got: {result}")
        all_passed = False

if all_passed:
    print("\nAll cases PASSED.")