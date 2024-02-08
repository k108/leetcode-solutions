# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.s = 0
        def dfs(root, num):
            if not root:
                return 0
            if not root.left and not root.right:
                self.s+=num*10+root.val
            dfs(root.left, num*10+root.val)
            dfs(root.right, num*10+root.val)
        dfs(root, 0)
        return self.s


        
