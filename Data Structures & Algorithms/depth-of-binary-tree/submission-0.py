# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # max_depth = 0

        def dfs(root, depth, max_depth):
            if not root:
                return depth
            depth += 1
            max_left = dfs(root.left, depth, max_depth)
            max_right = dfs(root.right, depth, max_depth)
            max_depth = max(max_left, max_right)
            return max_depth
            
        max_depth = dfs(root, 0, 0)
        return max_depth

