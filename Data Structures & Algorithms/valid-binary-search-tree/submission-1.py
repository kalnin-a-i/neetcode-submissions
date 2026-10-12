# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return None, None, True
            
            min_left, max_left, status_left = dfs(root.left)
            min_right, max_right, status_right = dfs(root.right)

            if not status_left or not status_right:
                return None, None, False
            
            status = (max_left is None or max_left < root.val) and ( min_right is None or min_right > root.val)
            # print(root.val, min_right, max_left, min_left, status)
            # print()
            min_ = min(root.val, min_left) if min_left is not None else root.val
            max_ = max(root.val, max_right) if max_right is not None else root.val
            # print(min_)
            return min_, max_, status

        _, _, ans = dfs(root)
        return ans