import unittest
from typing import Optional

class BiNode:
    def __init__(self, val: int):
        self.val = val
        self.node1: Optional["BiNode"] = None # left (BST), prev (DLL)
        self.node2: Optional["BiNode"] = None # right (BST), next (DLL)

def convert_bst_to_dll(root: Optional[BiNode]) -> Optional[BiNode]:
    if not root:
        return None

    head: Optional[BiNode] = None
    prev: Optional[BiNode] = None

    def in_order(curr: Optional[BiNode]) -> None:
        nonlocal head, prev

        # base case 
        if not curr: 
            return
    
        # 1. process left subtree
        in_order(curr.node1)

        # 2. Link previous node with current node
        if prev:
            prev.node2 = curr
            curr.node1 = prev
        else:
            head = curr
        # update the last visited node, at this place, after having visited a node
        # prev represents the node we just finished processing
        # since curr is fully processed before enter its right subtree, 
        # curr msut become prev, before any of its right subtree nodes are visited
        prev = curr
        # 3. process right subtree
        in_order(curr.node2)

    in_order(root)
    return head
    
    
# # =====================================================================
# # SOLUTION PLACEHOLDER
# # Replace or import your actual class & function here
# # =====================================================================
# class BiNode:
#     def __init__(self, val: int):
#         self.val = val
#         self.node1: Optional['BiNode'] = None  # prev / left
#         self.node2: Optional['BiNode'] = None  # next / right


# def convert_bst_to_dll(root: Optional[BiNode]) -> Optional[BiNode]:
#     """Converts a BST into an in-order doubly linked list in-place.
#     node1 points to prev, node2 points to next.
#     """
#     if not root:
#         return None

#     def helper(curr):
#         nonlocal prev_node, head
#         if not curr:
#             return

#         helper(curr.node1)

#         if prev_node:
#             prev_node.node2 = curr
#             curr.node1 = prev_node
#         else:
#             head = curr
#         prev_node = curr

#         helper(curr.node2)

#     head = None
#     prev_node = None
#     helper(root)
#     return head


# =====================================================================
# TEST SUITE
# =====================================================================
class TestBiNode(unittest.TestCase):

    def dll_to_list_and_verify(self, head: Optional[BiNode]) -> list[int]:
        """Traverses the doubly linked list forward and backward to verify pointer integrity."""
        values = []
        curr = head
        last = None

        while curr:
            values.append(curr.val)
            if curr.node2 is None:
                last = curr
            curr = curr.node2

        # Verify reverse pointers
        curr = last
        rev_values = []
        while curr:
            rev_values.append(curr.val)
            curr = curr.node1

        self.assertEqual(values, list(reversed(rev_values)), "Bidirectional links are broken!")
        return values

    def test_01_empty_tree(self):
        """Empty tree returns None."""
        self.assertIsNone(convert_bst_to_dll(None))

    def test_02_single_node(self):
        """Single curr returns itself with empty node1 and node2."""
        root = BiNode(10)
        head = convert_bst_to_dll(root)
        self.assertEqual(head.val, 10)
        self.assertIsNone(head.node1)
        self.assertIsNone(head.node2)

    def test_03_left_skewed_tree(self):
        """Left-skewed tree converts to sorted list."""
        root = BiNode(3)
        root.node1 = BiNode(2)
        root.node1.node1 = BiNode(1)

        head = convert_bst_to_dll(root)
        self.assertEqual(self.dll_to_list_and_verify(head), [1, 2, 3])

    def test_04_right_skewed_tree(self):
        """Right-skewed tree converts to sorted list."""
        root = BiNode(1)
        root.node2 = BiNode(2)
        root.node2.node2 = BiNode(3)

        head = convert_bst_to_dll(root)
        self.assertEqual(self.dll_to_list_and_verify(head), [1, 2, 3])

    def test_05_balanced_bst(self):
        """Balanced BST produces fully sorted doubly linked list."""
        root = BiNode(4)
        root.node1 = BiNode(2)
        root.node2 = BiNode(6)
        root.node1.node1 = BiNode(1)
        root.node1.node2 = BiNode(3)
        root.node2.node1 = BiNode(5)
        root.node2.node2 = BiNode(7)

        head = convert_bst_to_dll(root)
        self.assertEqual(self.dll_to_list_and_verify(head), [1, 2, 3, 4, 5, 6, 7])


# =====================================================================
# INFORMATIVE TEST RUNNER
# =====================================================================
def run_informative_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    print(f"\n{'='*75}\n TEST SUITE: CTCI 17.12 - BiNode (BST to DLL)\n{'='*75}")

    passed, failed, errors = 0, 0, 0

    for test in suite:
        test_name = test._testMethodName
        doc = (test._testMethodDoc or "").strip()
        desc = f"{test_name} -> {doc}" if doc else test_name

        result = unittest.TestResult()
        test.run(result)

        if result.wasSuccessful():
            print(f"  ✅ [PASS] {desc}")
            passed += 1
        elif result.failures:
            print(f"  ❌ [FAIL] {desc}")
            failed += 1
        elif result.errors:
            print(f"  ⚠️  [ERROR] {desc}")
            errors += 1

    total = passed + failed + errors
    pass_rate = (passed / total * 100) if total > 0 else 0.0

    print(f"\n{'-'*75}")
    print(f" EXECUTION SUMMARY:")
    print(f" Total Tests : {total}")
    print(f" Passed      : {passed} ✅")
    print(f" Failed      : {failed} ❌")
    print(f" Errors      : {errors} ⚠️")
    print(f" Success Rate: {pass_rate:.1f}%")
    print(f"{'='*75}\n")


if __name__ == "__main__":
    run_informative_tests(TestBiNode)