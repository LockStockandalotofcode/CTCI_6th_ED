# Assumption: 
# no link to parent nodes
# presence of node in the tree no guaranteed

from typing import Optional

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def covers(root: TreeNode, target: TreeNode) -> bool:
    if not root or not target:
        return False
    if root == target:
        return True
    return covers(root.left, target) or covers(root.right, target)

def fca_helper(root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root or root == p or root == q:
        return root

    # TOP-DOWN 
    p_on_left_result = covers(root.left, p)
    q_on_left_result = covers(root.left, q)

    # covering all 4 cases of 2 x 2 Truth Table
    if p_on_left_result != q_on_left_result:
        return root


    # APPROACH 1
    # if p_on_left_result and q_on_left_result:
    #     return fca_helper(root.left, p, q)
    # if not p_on_left_result and not q_on_left_result:
    #     return fca_helper(root.right, p, q)

    # APPROACH 2
    child_side = root.left if  p_on_left_result else root.right
    return fca_helper(child_side, p, q)
        
def find_fca(root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]) -> Optional[TreeNode]:
    if not covers(root, p) or not covers(root, q): return None
    return fca_helper(root, p, q)


# def check_if_ancestor()
def run_first_common_ancestor_tests():
    passed, failed = 0, 0
    print("\n" + "=" * 60)
    print("RUNNING CTCI 4.8: FIRST COMMON ANCESTOR TESTS")
    print("=" * 60)

    # Tree Construction:
    #          1
    #        /   \
    #       2     3
    #      / \     \
    #     4   5     6
    #        / \
    #       7   8
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    n4 = TreeNode(4)
    n5 = TreeNode(5, left=n7, right=n8)
    n6 = TreeNode(6)
    n2 = TreeNode(2, left=n4, right=n5)
    n3 = TreeNode(3, right=n6)
    root = TreeNode(1, left=n2, right=n3)

    orphan = TreeNode(99)  # Not attached to root

    # Format: (root, p, q, expected_ancestor_node, description)
    test_cases = [
        (root, n4, n8, n2, "LCA of leaf nodes across subtrees (4 and 8 -> 2)"),
        (root, n7, n8, n5, "LCA of sibling nodes (7 and 8 -> 5)"),
        (root, n4, n6, root, "LCA across main left and right subtrees (4 and 6 -> 1)"),
        (root, n2, n7, n2, "LCA where p is ancestor of q (2 and 7 -> 2)"),
        (root, n5, n5, n5, "LCA where p and q are the exact same node (5 and 5 -> 5)"),
        (root, n4, orphan, None, "q is an orphan node not present in tree"),
        (orphan, orphan, n4, None, "p is not present in orphan root tree"),
        (None, n4, n8, None, "Empty tree root"),
    ]

    # Skewed Tree Case: 10 -> 20 -> 30 -> 40
    s40 = TreeNode(40)
    s30 = TreeNode(30, left=s40)
    s20 = TreeNode(20, left=s30)
    s10 = TreeNode(10, left=s20)
    test_cases.append(
        (s10, s30, s40, s30, "Left-skewed list-like tree ancestor")
    )
    # p (n6) is on the right of root; q (n4) is on the left of root
    test_cases.append((root, n6, n4, root, "LCA where p is on right and q is on left"))

    for i, (tree_root, p, q, expected, desc) in enumerate(test_cases, 1):
        try:
            res = find_fca(tree_root, p, q)

            # Strict memory identity assertion
            assert res is expected, (
                f"Expected node reference {id(expected)} (val={expected.val if expected else None}), "
                f"got {id(res)} (val={res.val if res else None})"
            )

            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"4.8 SUMMARY: {passed} PASSED | {failed} FAILED | Total: {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_first_common_ancestor_tests()