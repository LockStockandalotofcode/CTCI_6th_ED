from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_subtree(t1: TreeNode, t2: TreeNode) -> bool:
    if t2 is None:
        return True
    if t1 is None and t2 is not None: 
        return False
        
    queue = deque([t1])
    while queue:
        curr = queue.popleft()
        if curr.val == t2.val:
            if check_identical_tree(curr, t2):
                return True
        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

    return False

def check_identical_tree(t1_node: TreeNode, t2_node: TreeNode) -> bool:
    if t1_node is None and t2_node is None:
        return True
    elif t1_node is None and t2_node is not None or t1_node is not None and t2_node is None:
        return False
    if t1_node.val != t2_node.val:
        return False
    if check_identical_tree(t1_node.left, t2_node.left) and check_identical_tree(t1_node.right, t2_node.right):
        return True

    return False

def run_check_subtree_tests():
    # Construct Base Tree T1
    #          1
    #        /   \
    #       2     3
    #      / \
    #     4   5
    #        /
    #       6
    t1 = TreeNode(
        1,
        left=TreeNode(
            2, left=TreeNode(4), right=TreeNode(5, left=TreeNode(6))
        ),
        right=TreeNode(3),
    )

    # Valid Subtree T2 (Rooted at Node 2)
    t2_valid = TreeNode(2, left=TreeNode(4), right=TreeNode(5, left=TreeNode(6)))

    # Invalid Subtree T2 (Matching values, but missing leaf Node 6)
    t2_missing_leaf = TreeNode(2, left=TreeNode(4), right=TreeNode(5))

    # Invalid Subtree T2 (Matching structure, wrong value)
    t2_wrong_val = TreeNode(2, left=TreeNode(4), right=TreeNode(99))

    test_cases = [
        (t1, None, True, "t2 is None (Empty tree is always a subtree)"),
        (None, TreeNode(1), False, "t1 is None, t2 is non-empty"),
        (t1, t1, True, "Identical tree memory instance"),
        (t1, t2_valid, True, "Valid complete subtree match"),
        (
            t1,
            t2_missing_leaf,
            False,
            "Matching values but truncated subtree structure",
        ),
        (t1, t2_wrong_val, False, "Matching structure but mismatched value"),
        (
            TreeNode(1, left=TreeNode(2)),
            TreeNode(2, left=TreeNode(1)),
            False,
            "Inverted tree values",
        ),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 4.10: CHECK SUBTREE TESTS")
    print("=" * 60)

    for i, (tree1, tree2, expected, desc) in enumerate(test_cases, 1):
        try:
            res = is_subtree(tree1, tree2)
            assert (
                res == expected
            ), f"Expected {expected} for {desc}, got {res}"
            print(f"  [PASS] Test {i:02d}: {desc}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: {desc} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"4.10 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_check_subtree_tests()