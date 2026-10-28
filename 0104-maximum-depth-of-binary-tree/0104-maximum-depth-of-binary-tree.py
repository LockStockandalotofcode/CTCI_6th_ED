# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        # iterative bfs
        if not root:
            return 0
        
        queue = deque([root])

        depth = 0
        while queue:
            level_size = len(queue)
            
            for _ in range(level_size):
                curr = queue.popleft()
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            depth += 1
            # stores depth of the level processed

        return depth