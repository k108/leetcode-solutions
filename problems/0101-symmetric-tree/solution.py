# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(s, t):
            if not s and not t:
                return True
            else:
                if s and t and s.val == t.val:
                    return dfs(s.left, t.right) and dfs(s.right, t.left) 
                else:
                    return False
        return dfs(root.left, root.right)
        
