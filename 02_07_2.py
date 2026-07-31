from typing import Optional, List, Set, Tuple

# implementation of a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_intersection(head1: ListNode | None, head2: ListNode | None) -> ListNode | None:
    if not head1 or not head2:
        return None 

    p1, p2 = head1, head2

    # this loop continues only until both nodes point to the exact same refernce 
    # (either the intersecting Node, or Both are None )

    # if they don't intersect - 2 cases: both have same length or different length
    # case 1: same length -- then both reach the tail node None at the same time
    # Case 2: different length -- then pointers go through the other linked list, before both reach the end None node simultaneously

    # using None for conditional check for loop allows for breaking from the loop, without relying on next is None and using manual flag to track whether to break the loop
    # because using .next is None, skips the None node altogether

    while p1 != p2:
        p1 = head2 if p1 is None else p1.next
        p2 = head1 if p2 is None else p2.next

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