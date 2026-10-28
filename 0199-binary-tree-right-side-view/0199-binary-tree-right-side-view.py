# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            size = len(queue)
            for i in range(size):
                curr = queue.popleft()
                if i == (size - 1):
                    result.append(curr.val)
                
                # enqueue child nodes if existing
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

        return result