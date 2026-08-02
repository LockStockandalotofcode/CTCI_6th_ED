# recursive solution

# implementation of TreeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def validate_bst(root: TreeNode) -> bool:
    # base case 
    if not root: return True

    # safely assigning child nodes, before recursion
    left_val = root.left.val if root.left else float('-inf')
    right_val = root.right.val if root.right else float('inf')

    return validate_bst(root.left) and validate_bst(root.right) and (left_val <= root.val < right_val)

def run_validate_bst_tests():
    # 1. Valid BST
    #       10
    #      /  \
    #     5    15
    t_valid = TreeNode(10, TreeNode(5), TreeNode(15))

    # 2. Locally Valid, Globally Invalid BST (12 is on left of 10, violating ancestor bound)
    #       10
    #      /  \
    #     5    15
    #      \
    #       12
    t_globally_invalid = TreeNode(
        10, TreeNode(5, right=TreeNode(12)), TreeNode(15)
    )

    # 3. Direct Invariant Violation
    t_invalid_direct = TreeNode(10, TreeNode(20), TreeNode(15))

    test_cases = [
        (None, True),
        (TreeNode(5), True),
        (t_valid, True),
        (t_globally_invalid, False),
        (t_invalid_direct, False),
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 4.5: VALIDATE BST TESTS")
    print("=" * 60)

    for i, (root, expected) in enumerate(test_cases, 1):
        try:
            res = validate_bst(root)
            assert res == expected, f"Expected {expected}, got {res}"
            print(f"  [PASS] Test {i:02d}: Expected {expected} -> Got {res}")
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"4.5 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_validate_bst_tests()