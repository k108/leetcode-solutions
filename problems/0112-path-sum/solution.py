# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.result = False
        def dfs(root, s, targetSum):
            if not root:
                return 0
            if root.left == None and root.right == None:
                if root.val+s == targetSum:
                    self.result = True

            dfs(root.left, s+root.val, targetSum)
            dfs(root.right, s+root.val, targetSum)
        dfs(root, 0, targetSum)
        return self.result
        
        
