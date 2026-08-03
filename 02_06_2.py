from typing import List, Optional

# implementation of linked List Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome_list(head: ListNode) -> bool:
    if not head or not head.next: return True

    fast = head
    slow = head
    new_head = None

    # reverse the linked list's first half 
    # unlink the two halves once the middle node is reached,  then make a separate new list for first half, and it is reversed
    # compare the two list halves


    while fast and fast.next:
        fast = fast.next.next
        # save slow node before adding to first_half_reversed list
        next_temp = slow.next
        
        # reverse the two nodes
        slow.next = new_head
        new_head = slow
        
        # increment the two pointers, slow by the temporary saved next node
        slow = next_temp

    # if fast is not None: # odd length list, skip the middle node
    if fast is not None: 
        slow = slow.next

    # save the second half's head
    head2 = slow

    # correct the head of first_half_reversed
    head1 = new_head

    # traverse the two halves together
    while head1 and head2:
        if head1.val != head2.val: return False
        head1 = head1.next
        head2 = head2.next

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