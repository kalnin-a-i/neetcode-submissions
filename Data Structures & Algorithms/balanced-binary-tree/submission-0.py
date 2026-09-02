# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, depth):
            if not root:
                return True, depth
            b_r, depth_r = dfs(root.right, depth + 1)
            b_l, depth_l = dfs(root.left, depth + 1)
            balanced = b_l and b_r and (abs(depth_l - depth_r) <= 1)
            height = max(depth_l, depth_r)
            return balanced, height

        ans, _ = dfs(root, 0)
        return ans
            