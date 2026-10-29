# Definition for a binary tree root.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        # inorder hashmap- to locate index of root in inorder array, gives left and right subtrees of this root
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        # global preorder index, nodes are made as  per this
        pre_idx = 0

        def helper(in_start: int, in_end: int) -> Optional[TreeNode]:
            nonlocal pre_idx

            # base case termination, when a subtree is done being converted into the tree nodes
            if in_start > in_end:
                return None
            # execute current root
            node_val = preorder[pre_idx]
            root = TreeNode(node_val)
            pre_idx += 1
            # recursively call helper function for left and right subtrees
            inorder_idx = inorder_map[node_val]
            root.left = helper(in_start, inorder_idx - 1)
            root.right = helper(inorder_idx + 1, in_end)
            return root

        return helper(0, len(inorder) - 1)