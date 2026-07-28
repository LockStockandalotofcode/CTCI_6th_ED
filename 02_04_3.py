from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head: ListNode | None, x: int) -> ListNode | None:
    # base case
    if not head:
        return None
    
    current = head
    tail = head

    # appending less nodes at the very start, and greater nodes at very tail
    while current:
        # save the nextnode, temporarily deattach from the linked list
        next_node = current.next
        current.next = None

        # do the rearragning of node, as per rule (< or >= x)
        if current.val < x:
            current.next = head
            head = current
        else:
            tail.next = current
            tail = current

        current = next_node # moving to next node in original linked list

    # just to be safe, for the cases all nodes < x, tail points to head, when it should point to None
    if tail.next is not None:
        tail.next = None

    return head
    
def build_linked_list(vals: List[int]) -> Optional[ListNode]:
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    res = []
    curr = head
    while curr:
        res.append(curr.val)
        curr = curr.next
    return res


def run_partition_tests():
    test_cases = [
        # (input_list, partition_x)
        ([], 5),  # Empty List
        ([10], 5),  # Single Element
        ([3, 5, 8, 5, 10, 2, 1], 5),  # Standard CTCI case
        ([1, 2, 3, 4], 5),  # All elements < x
        ([5, 6, 7, 8], 5),  # All elements >= x
        ([5, 5, 5, 5], 5),  # All elements identical to x
        ([9, 1, 8, 2, 7, 3], 5),  # Interleaved values
        ([-5, 10, -2, 0, 3], 0),  # Negative numbers & zeroes
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 2.4: PARTITION TESTS")
    print("=" * 60)

    for i, (vals, x) in enumerate(test_cases, 1):
        head = build_linked_list(vals)
        try:
            res_head = partition(head, x)
            res_vals = linked_list_to_list(res_head)

            # 1. Verify multiset preservation (no elements added/lost)
            assert sorted(res_vals) == sorted(
                vals
            ), f"Elements lost or corrupted! Expected multiset {sorted(vals)}, got {sorted(res_vals)}"

            # 2. Verify partition property: Once a node >= x is seen, no node < x can appear
            seen_geq = False
            for val in res_vals:
                if val >= x:
                    seen_geq = True
                elif val < x and seen_geq:
                    assert False, (
                        f"Partition violated! Element {val} (< {x}) appeared"
                        f" after an element >= {x} in {res_vals}"
                    )

            print(
                f"  [PASS] Test {i:02d}: x={x:<2} | Input: {vals} -> Output:"
                f" {res_vals}"
            )
            passed += 1
        except Exception as e:
            print(
                f"  [FAIL] Test {i:02d}: x={x:<2} | Input: {vals} -> ERROR:"
                f" {e}"
            )
            failed += 1

    print("-" * 60)
    print(
        f"2.4 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_partition_tests()