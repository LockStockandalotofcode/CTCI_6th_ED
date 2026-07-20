# PROBLEM 02_01
# FOLLOW-UP
# WITHOUT EXTRA DATA STR, HASHTABLE & HASHSET
# USING 2 POINTERS

# # LOGIC
# 1 ONE ptr traverses the entire list
# 2 second ptr traverses subsequent list to remove duplicates of this value

# # assumptions clarifications
# singly vs doubly linked 

# TEST_CASES
test_cases = (
	# normal case 
	([1, 2, 4, 2, 2, 5, 1], [1, 2, 4, 5]),
    ([1, 5, 4, 5, 5, 4, 5], [1, 5, 4]),
	# empty case
    ([], []),
    ([1, 1, 1, 1, 1, 1], [1]),
    ([1, 2, 3, 2], [1, 2, 3]),
    ([1, 2, 2, 3], [1, 2, 3]),
    ([1, 1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [1, 2, 3])
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
	
def remove_dups(linked_list: LinkedList) -> LinkedList:
	if not linked_list.head:
		return linked_list
	prev_node = curr_node = linked_list.head
	
	while curr_node:
		prev_node = curr_node
		running_node = curr_node.next
		while running_node:
			# if duplicate
			if running_node.val == curr_node.val:
				prev_node.next = running_node.next
				running_node = running_node.next
			# if not duplicate
			else:
				prev_node = running_node
				running_node = running_node.next
		curr_node = curr_node.next

	return linked_list

# testing 
print("Running test cases: ")
all_passed = True

for idx, (input_values, exp_output) in enumerate(test_cases, 1):
	linked_list = LinkedList(input_values)
	result_linked_list = remove_dups(linked_list)
	result = result_linked_list.values()
	if result == exp_output:
		print(f"passed Test {idx}.")
	else:
		print(f"failed Test {idx} - Input: {input_values} | Expected: {exp_output} | Got: {result}")
		all_passed = False

if all_passed == True:
	print("\n All cases PASSED.")