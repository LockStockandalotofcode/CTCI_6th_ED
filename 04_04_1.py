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

    height_left = get_height_subtree(root.left)
    height_right = get_height_subtree(root.right)

    # differentiating bool False from int 0, because they usually are not distinguished in the if conditional test: if not number
    if not height_left and type(height_left) is bool:
        return False
    if not height_right and type(height_right) is bool:
        return False

    if abs(height_right - height_left) > 1:
        return False

    return True

def get_height_subtree(node : TreeNode | None) -> int | bool:
    if not node:
        return 0

    height_left = get_height_subtree(node.left)
    height_right = get_height_subtree(node.right)
    if abs(height_right - height_left) > 1:
        return False

    height = max(height_left, height_right) + 1
    return height

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