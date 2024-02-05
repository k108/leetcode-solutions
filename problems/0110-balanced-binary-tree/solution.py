# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height_balanced = True
        def dfs(root):
            if not root:
                return 0
            
            left_height = dfs(root.left)
            right_height = dfs(root.right)
            if abs(left_height - right_height) > 1:
                self.height_balanced = False
            return max(left_height, right_height) + 1
        dfs(root)
        return self.height_balanced
        
