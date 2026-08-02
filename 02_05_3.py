from typing import Optional, List

# implementation of linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def sum_lists(head1: ListNode, head2: ListNode, carry=0) -> ListNode:
    # base condition - stop only when both lists and the carry al are exhausted
    if not head1 and not head2 and carry == 0: return None

    val1 = head1.val if head1 else 0
    val2 = head2.val if head2 else 0
    carry = carry
    total = val1 + val2 + carry

    carry = total // 10
    result = ListNode(total % 10)

    # to avoid accessing node.next for a node that doesn't exist, safely use this mechanism to  extract .next node before making the recursive call
    next1 = head1.next if head1 else None
    next2 = head2.next if head2 else None
    
    result.next = sum_lists(next1, next2, carry) 
    return result

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


def run_sum_lists_tests():
    test_cases = [
        # (list1_vals, list2_vals, expected_sum_vals)
        # 617 + 295 = 912 -> [2, 1, 9]
        ([7, 1, 6], [5, 9, 2], [2, 1, 9]),
        # 99 + 1 = 100 -> [0, 0, 1]
        ([9, 9], [1], [0, 0, 1]),
        # 0 + 0 = 0 -> [0]
        ([0], [0], [0]),
        # 123 + [] = 123 -> [3, 2, 1]
        ([3, 2, 1], [], [3, 2, 1]),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 2.5: SUM LISTS TESTS")
    print("=" * 60)

    for i, (v1, v2, expected) in enumerate(test_cases, 1):
        l1, l2 = build_linked_list(v1), build_linked_list(v2)
        try:
            res_head = sum_lists(l1, l2)
            res_vals = linked_list_to_list(res_head)
            assert (
                res_vals == expected
            ), f"For {v1} + {v2}, expected {expected}, got {res_vals}"
            print(f"  [PASS] Test {i:02d}: {v1} + {v2} -> {res_vals}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"2.5 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_sum_lists_tests()