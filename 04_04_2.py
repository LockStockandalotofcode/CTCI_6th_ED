# implementation of TreeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right

# CODE
def is_balanced(root : TreeNode | None) -> bool:
    if not root:
        return True
    _, balanced = get_height_subtree(root)
    return balanced

def get_height_subtree(node : TreeNode | None) -> tuple[int, bool]:
    if not node: 
        # here we shouldn't pass None for height because this handles a node next to a leaf node, so considered in height calculation
        # we don't care about height only when the tree is unbalanced, as in the following conditional check
        return (0, True)

    height_left, left_balanced = get_height_subtree(node.left)
    height_right, right_balanced = get_height_subtree(node.right)
    if not left_balanced or not right_balanced:
        return (0, False)

    balanced = abs(height_right - height_left) <= 1
    height = max(height_left, height_right) + 1
    return (height, balanced)

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