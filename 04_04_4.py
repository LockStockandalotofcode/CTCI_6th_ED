# implementation of TreeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right

# CODE
def is_balanced(root : TreeNode | None) -> bool:
    # base case
    if not root:
        return True

    # this checks parent tree's balanced or not(in this case if root node is balanced), it could parent node is balanced, but the a child node is unbalanced as in test_case 4
    # thus we need to change our order of traversal from child nodes to parent node or pre-order traversal which is essentially this
    # left -> right -> root
    # bottom-up traversal

    # building stack for post-order traversal - 2 stack pass, one for building the stack, one for exceuting nodes
    stack = [root]
    post_order = []
    while stack:
        node = stack.pop()
        post_order.append(node)
        if node.left: stack.append(node.left)
        if node.right: stack.append(node.right)
    
    # evaluate nodes first child node then parent node: postorder traversal
    # hashing once evaluated nodes' heights, with the help of hashmap
    heights = {}
    for node in reversed(post_order):
        left_h = heights.get(node.left, 0)
        right_h = heights.get(node.right, 0)

        if abs(left_h - right_h) > 1: return False

        # hash for later, quick O(1) lookup
        heights[node] = 1 + max(left_h, right_h)

    return True
  
def run_check_balanced_tests():
    # Helper tree generators
    # 1. Balanced Tree
    #       1
    #      / \
    #     2   3
    t_balanced = TreeNode(1, TreeNode(2), TreeNode(3))

    # 2. Unbalanced Tree (Left Skewed)
    #       1
    #      /
    #     2
    #    /
    #   3
    t_unbalanced = TreeNode(1, TreeNode(2, TreeNode(3)))

    # 3. Complex Balanced Tree
    #          1
    #        /   \
    #       2     3
    #      / \   /
    #     4   5 6
    t_complex_balanced = TreeNode(
        1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6))
    )

    # 4. Subtle Unbalanced Tree (Subtree height difference > 1 deep down)
    #          1
    #        /   \
    #       2     3
    #      /
    #     4
    #    /
    #   5
    t_subtle_unbalanced = TreeNode(
        1, TreeNode(2, TreeNode(4, TreeNode(5))), TreeNode(3)
    )

    test_cases = [
        (None, True),  # Empty tree
        (TreeNode(10), True),  # Single node
        (t_balanced, True),
        (t_unbalanced, False),
        (t_complex_balanced, True),
        (t_subtle_unbalanced, False),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 4.4: CHECK BALANCED TESTS")
    print("=" * 60)

    for i, (root, expected) in enumerate(test_cases, 1):
        try:
            res = is_balanced(root)
            assert res == expected, f"Expected {expected}, got {res}"
            print(f"  [PASS] Test {i:02d}: Expected {expected} -> Got {res}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"4.4 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_check_balanced_tests()