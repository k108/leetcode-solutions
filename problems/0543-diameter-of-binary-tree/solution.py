# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_depth = 0
        def dfs(root):
            if not root:
                return 0
            
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            self.max_depth = max(self.max_depth, left_depth+right_depth)
            return max(left_depth, right_depth) + 1
        dfs(root)
        return self.max_depth

        
