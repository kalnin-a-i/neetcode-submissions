# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(root, depth):
            if not root:
                return depth, 0
            
            depth_left, diameter_left = dfs(root.left, depth + 1)
            depth_right, diameter_right = dfs(root.right, depth + 1)
            diameter = max(diameter_right, diameter_left, depth_left + depth_right - 2 * (depth + 1))
    
            return max(depth_left, depth_right), diameter

        depth, diameter = dfs(root, 0)
        return diameter