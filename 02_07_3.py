from typing import Optional, List, Set, Tuple

# implementation of a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_length_and_tail(head: ListNode) -> tuple[int, ListNode]:
    if not head: return (0, None)
    length = 1
    ptr = head
    while ptr.next:
        ptr = ptr.next
        length += 1
    return (length, ptr)

def advance_by(p: ListNode, steps: int) -> ListNode:
    for _ in range(steps):
        p = p.next
    return p
    
def find_intersection(head1: ListNode | None, head2: ListNode | None) -> ListNode | None:
    if not head1 or not head2:
        return None 
        
    # intersecting linked lists always have the same tail, or rather same linked list from the intersecting node onwards
    # get tail nodes first, if they match, intersection must exist, otherwise not
    len1, tail1 = get_length_and_tail(head1)
    len2, tail2 = get_length_and_tail(head2)

    p1, p2 = head1, head2

    if tail1 != tail2:
        return None

    if len1 > len2:
        p1 = advance_by(p1, len1 - len2)
        
    if len2 > len1:
        p2 = advance_by(p2, len2 - len1)
    
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next

    return p1

def build_linked_list(vals: List[int]) -> ListNode | None:
    if not vals: return None
    head = ListNode(vals[0])
    curr = head
    for v in vals[1: ]:
        curr.next = ListNode(v)
        curr = curr.next
    return head

def run_intersection_tests():
    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 2.7: INTERSECTION TESTS")
    print("=" * 60)

    # Test 1: Non-intersecting lists with identical values
    try:
        l1 = build_linked_list([1, 2, 3])
        l2 = build_linked_list([1, 2, 3])
        res = find_intersection(l1, l2)
        assert (
            res is None
        ), "Identical value lists with different nodes returned an intersection!"
        print(
            "  [PASS] Test 01: Distinct Nodes with Same Values (No"
            " Intersection)"
        )
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 01 -> ERROR: {e}")
        failed += 1

    # Test 2: Valid Intersection in Middle
    try:
        shared = build_linked_list([7, 8, 9])
        l1 = ListNode(1, ListNode(2, shared))
        l2 = ListNode(3, shared)
        res = find_intersection(l1, l2)
        assert (
            res is shared
        ), f"Expected reference identity {shared}, got {res}"
        print("  [PASS] Test 02: Valid Intersection in Middle")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 02 -> ERROR: {e}")
        failed += 1

    # Test 3: Completely Shared List
    try:
        l1 = build_linked_list([10, 20])
        res = find_intersection(l1, l1)
        assert res is l1, "Same list identity test failed!"
        print("  [PASS] Test 03: Complete List Identity Match")
        passed += 1
    except Exception as e:
        print(f"  [FAIL] Test 03 -> ERROR: {e}")
        failed += 1

    print("-" * 60)
    print(f"2.7 SUMMARY: {passed} PASSED | {failed} FAILED | Total: 3")
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_intersection_tests()