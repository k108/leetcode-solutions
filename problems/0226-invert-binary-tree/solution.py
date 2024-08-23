# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current_node = root
        def dfs(current_node):
            if not current_node:
                return
                
            current_node.left, current_node.right = current_node.right, current_node.left
            dfs(current_node.left)
            dfs(current_node.right)
        
        dfs(current_node)
        return root
        


        


        
