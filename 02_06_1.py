from typing import List, Optional

# first reach middle node: by 2-pointer approach, alongwith appending all nodes of slow pointer into a list
# when middle node is reached, compare next node and stack.pop()

# implementation of linked List Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome_list(head: ListNode) -> bool:
    if not head or not head.next: return True

    fast = head
    slow = head
    first_half_nodes = [] 

    while fast and fast.next:
        first_half_nodes.append(slow.val)
        slow = slow.next

        fast = fast.next.next

    # if fast is not None: length of linked is odd
    # if fast is  None: length of linked is even
    # slow stops at middle node after this loop stops iterating, for even length linked list (right node of the 2 centre nodes)

    # for odd length linked list we need to move slow node by 1, that is to skip the only middle node
    if fast is not None: # fast is None for even length list # for odd length list, fast is not None, fast.next is None, we move slow pointer one ahead
        slow = slow.next

    while first_half_nodes: # or loop until slow pointer reaches the end 
        if slow.val != first_half_nodes.pop():
            return False
        slow = slow.next


    return True

def build_linked_list(vals: List[int]) -> Optional[ListNode]:
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def run_palindrome_list_tests():
    test_cases = [
        ([], True),
        ([1], True),
        ([1, 1], True),
        ([1, 2], False),
        ([1, 2, 1], True),
        ([1, 2, 2, 1], True),
        ([1, 2, 3, 2, 1], True),
        ([1, 2, 3, 4, 5], False),
        ([1, 2, 3, 3, 1], False),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 2.6: PALINDROME LINKED LIST TESTS")
    print("=" * 60)

    for i, (vals, expected) in enumerate(test_cases, 1):
        head = build_linked_list(vals)
        try:
            res = is_palindrome_list(head)
            assert (
                res == expected
            ), f"For list {vals}, expected {expected}, got {res}"
            print(f"  [PASS] Test {i:02d}: {vals} -> {res}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {vals} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"2.6 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_palindrome_list_tests()