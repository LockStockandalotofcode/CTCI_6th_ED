from typing import Optional

# LinkedList Implementation
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# CODE 
def kth_to_last(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # Returns the k-th to last node (1-indexed: k=1 is last node).
    # Returns None if k is invalid or out of bounds.
    
    # base case
    if not head or k <= 0:
        return

    # approach 2 first get size of linked list n, then get (n-k+1) th node from the beginning
    ptr1 = head
    size = 1

    while ptr1.next:
        ptr1 = ptr1.next
        size += 1

    if k > size:
        return 

    ptr1 = head
    for _ in range(1, size - k + 1):
        ptr1 = ptr1.next

    return ptr1.val

def build_linked_list(vals: list[int]) -> Optional[ListNode]:
    if not vals:
        return None
    head = ListNode(vals[0])
    curr = head
    for v in vals[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


def run_kth_to_last_tests():
    test_cases = [
        # (input_list, k, expected_val)
        ([], 1, None),  # Empty List
        ([10], 1, 10),  # Single element, k=1
        ([10], 2, None),  # Single element, k out of bounds
        ([1, 2, 3, 4, 5], 1, 5),  # Last element
        ([1, 2, 3, 4, 5], 5, 1),  # First element
        ([1, 2, 3, 4, 5], 3, 3),  # Middle element
        ([1, 2, 3, 4, 5], 6, None),  # k > length
        ([1, 2, 3, 4, 5], 0, None),  # Invalid k <= 0
        ([1, 2, 3, 4, 5], -2, None),  # Invalid k < 0
    ]

    passed = 0
    failed = 0
    print("=" * 60)
    print("RUNNING CTCI 2.2: KTH TO LAST TESTS")
    print("=" * 60)

    for i, (vals, k, expected_val) in enumerate(test_cases, 1):
        head = build_linked_list(vals)
        try:
            res = kth_to_last(head, k)

            # Accept both returning a ListNode or returning raw value
            res_val = res.val if hasattr(res, "val") else res

            if expected_val is None:
                assert (
                    res_val is None
                ), f"Expected None for k={k} on {vals}, got {res_val}"
            else:
                assert (
                    res_val == expected_val
                ), f"Expected value {expected_val} for k={k}, got {res_val}"

            print(
                f"  [PASS] Test {i:02d}: list={vals}, k={k} ->"
                f" {res_val}"
            )
            passed += 1
        except Exception as e:
            print(
                f"  [FAIL] Test {i:02d}: list={vals}, k={k} -> ERROR: {e}"
            )
            failed += 1

    print("-" * 60)
    print(
        f"2.2 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_kth_to_last_tests()