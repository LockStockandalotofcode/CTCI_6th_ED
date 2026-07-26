from typing import Optional

# tree implementation
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# CODE
def minimal_tree(array: list[int]) -> TreeNode | None:
    # sorted array -> inorder traversal
    # all we need is root node to build the BST, that would be the middle node in inorder traversal

    # base case
    if not array:
        return 

    # if len(array) == 1:
    #     return TreeNode(array[0])

    # pick middle element for rootnode: that helps with the tree being minimal, a normal BST could have any node as its root 
    # even size : len // 2
    # odd size : len // 2
    mid = len(array) // 2

    # recursively build left and right subtrees
    root = TreeNode(array[mid])
    slice_left = slice(mid)
    slice_right = slice(mid + 1, len(array))
    root.left = minimal_tree(array[slice_left])
    root.right = minimal_tree(array[slice_right])

    return root

def get_tree_height(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(get_tree_height(root.left), get_tree_height(root.right))


def inorder_traversal(root: Optional[TreeNode], res: list[int]) -> None:
    if not root:
        return
    inorder_traversal(root.left, res)
    res.append(root.val)
    inorder_traversal(root.right, res)


def run_minimal_tree_tests():
    test_cases = [
        [],  # Empty Case
        [1],  # 1 Element (Height 1)
        [1, 2],  # 2 Elements (Height 2)
        [1, 2, 3],  # 3 Elements (Height 2)
        [1, 2, 3, 4],  # 4 Elements (Height 3)
        [-10, -5, 0, 5, 9, 12, 15],  # 7 Elements (Height 3)
        list(range(1, 16)),  # 15 Elements (Height 4)
        list(range(1, 17)),  # 16 Elements (Height 5)
    ]

    passed = 0
    failed = 0
    print("=" * 60)
    print("RUNNING CTCI 4.2: MINIMAL TREE TESTS")
    print("=" * 60)

    for i, arr in enumerate(test_cases, 1):
        try:
            root = minimal_tree(arr)

            # 1. Check Empty Case
            if not arr:
                assert (
                    root is None
                ), f"Expected None for empty array, got node with val {getattr(root, 'val', None)}"
            else:
                assert (
                    root is not None
                ), f"Expected tree root for {arr}, got None"

                # 2. Verify BST In-Order Traversal Matches Sorted Array
                traversed = []
                inorder_traversal(root, traversed)
                assert traversed == arr, (
                    "In-order traversal of BST does not match original sorted"
                    f" array!\nExpected: {arr}\nGot:      {traversed}"
                )

                # 3. Verify Minimal Height Property
                max_allowed_height = len(arr).bit_length()
                actual_height = get_tree_height(root)
                assert actual_height <= max_allowed_height, (
                    f"Tree height {actual_height} exceeds minimal height bound"
                    f" {max_allowed_height} for N={len(arr)}"
                )

            print(
                f"  [PASS] Test {i:02d}: N={len(arr)} -> Height"
                f" {get_tree_height(root)} (Max Allowed:"
                f" {len(arr).bit_length()})"
            )
            passed += 1
        except Exception as e:
            print(f"  [FAIL] Test {i:02d}: N={len(arr)} -> ERROR: {e}")
            failed += 1

    print("-" * 60)
    print(
        f"4.2 SUMMARY: {passed} PASSED | {failed} FAILED | Total:"
        f" {len(test_cases)}"
    )
    print("=" * 60 + "\n")

if __name__ == "__main__":
    run_minimal_tree_tests()