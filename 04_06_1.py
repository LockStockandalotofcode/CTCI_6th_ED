class TreeNodeWithParent:
    def __init__(self, val: int = 0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

# BST
def inorder_successor(node: TreeNodeWithParent):
    if not node and not node.right and node.parent:
        return None

    # case 2: node has no parents - next is its right child (root node)
    # case 1: node is left child - next is its parent 
    # case 3: node is right child - climbing up until an ancestor is found that is a left child

    if not node.parent:
        # if root node, successor is leftmost node of right subtree
        successor = node.right
        while successor and successor.left:
            successor = successor.left
        return successor

    if node == node.parent.left:
        return node.right if node.right else node.parent
    if node == node.parent.right:
        ancestor = node
        while ancestor.parent and ancestor != ancestor.parent.left:
            # climb up the ancestors
            ancestor = ancestor.parent 

        return ancestor.parent if ancestor.parent else None

def run_inorder_successor_tests():
    # Build a BST with explicit parent pointers:
    n20 = TreeNodeWithParent(20)
    n10 = TreeNodeWithParent(10, parent=n20)
    n30 = TreeNodeWithParent(30, parent=n20)
    n20.left, n20.right = n10, n30
    n5 = TreeNodeWithParent(5, parent=n10)
    n15 = TreeNodeWithParent(15, parent=n10)
    n10.left, n10.right = n5, n15
    #          20
    #        /    \
    #       10     30
    #      /  \   /
    #     5   15 25   <-- Added 25

    n25 = TreeNodeWithParent(25, parent=n30)
    n30.left = n25

    test_cases = [
        (n5, n10),  # Successor of 5 (leaf) is parent 10
        (n10, n15),  # Successor of 10 (has right child 15) is 15
        (n15, n20),  # Successor of 15 (rightmost leaf of left subtree) is root 20
        (n20, n25),  # Successor of 20 is min node of right subtree (30)
        (n30, None),  # Successor of 30 (largest element) is None
    ]

    passed, failed = 0, 0
    print("=" * 60)
    print("RUNNING CTCI 4.6: IN-ORDER SUCCESSOR TESTS")
    print("=" * 60)

    for i, (target, expected) in enumerate(test_cases, 1):
        try:
            res = inorder_successor(target)
            expected_val = expected.val if expected else None
            actual_val = res.val if res else None
            assert res is expected, (
                f"For node {target.val}, expected successor node"
                f" {expected_val}, got {actual_val}"
            )
            print(
                f"  [PASS] Test {i:02d}: Node {target.val} -> Successor:"
                f" {actual_val}"
            )
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: Node {target.val} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"4.6 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_inorder_successor_tests()