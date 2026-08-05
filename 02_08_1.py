from typing import List, Optional, Tuple

# implementation of linked List
class ListNode:
    def __init__(self, val: int = 0, next=None):
        self.val = val 
        self.next = next

def detect_loop(head: ListNode | None) -> ListNode | None:
    if not head: return None

    # check if loop exists
    # condition: fast = slow somewhere,  
    # if no loop exists, fast becomes none, loop breaks
    fast = head
    slow = head
    loop_exists = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            loop_exists = True
            break
        # this check must be done after atleast one iteration, so that at the head node, same starting point for both, it doesnot make a false assumption of loop presence

    # else return None
    if loop_exists:
        # find the the beginning of loop
        # as per my observation, its always 2 nodes before the loop begins that slow = fast 
        fast = fast.next.next
        return fast

    else:
        return None

def create_cyclic_list(
    vals: List[int], loop_index: int
) -> Tuple[Optional[ListNode], Optional[ListNode]]:
    """Helper: Creates a linked list.

    If loop_index >= 0, the tail points to the node at index loop_index.
    Returns (head, expected_loop_node).
    """
    if not vals:
        return None, None

    nodes = [ListNode(v) for v in vals]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    expected_node = None
    if loop_index >= 0 and loop_index < len(nodes):
        nodes[-1].next = nodes[loop_index]
        expected_node = nodes[loop_index]

    return nodes[0], expected_node


def run_loop_detection_tests():
    passed, failed = 0, 0
    print("\n" + "=" * 60)
    print("RUNNING CTCI 2.8: LOOP DETECTION TESTS")
    print("=" * 60)

    # (values, loop_start_index, description)
    test_cases = [
        ([], -1, "Empty list"),
        ([1], -1, "Single node, no loop"),
        ([1], 0, "Single node, pointing to itself"),
        ([1, 2], -1, "Two nodes, no loop"),
        ([1, 2], 0, "Two nodes, loop back to head"),
        ([1, 2], 1, "Two nodes, loop back to self (tail loop)"),
        ([1, 2, 3, 4, 5], -1, "Odd length list, no loop"),
        ([1, 2, 3, 4, 5, 6], -1, "Even length list, no loop"),
        ([1, 2, 3, 4, 5], 2, "Loop starting in the middle (node 3)"),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, "Full circular list starting at head"),
        (
            [10, 20, 30, 40, 50, 60],
            4,
            "Loop at penultimate node (long tail, short loop)",
        ),
    ]

    for i, (vals, loop_idx, desc) in enumerate(test_cases, 1):
        head, expected_node = create_cyclic_list(vals, loop_idx)
        try:
            res_node = detect_loop(head)

            # Strict identity check
            assert res_node is expected_node, (
                f"Expected node memory address {id(expected_node)} "
                f"(val={expected_node.val if expected_node else None}), "
                f"got {id(res_node)} (val={res_node.val if res_node else None})"
            )

            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"2.8 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_loop_detection_tests()