# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        
        
        queue = deque()
        queue.append((root, 0))
        answer = []
        k = 0
        while queue:
            v, level = queue.popleft()
            if v:
                if len(answer) < level + 1:
                    answer.append([])
                    answer[level].append(v.val)
                else:
                    answer[level].append(v.val)
                queue.append((v.left, level + 1))
                queue.append((v.right, level + 1))
        return answer

