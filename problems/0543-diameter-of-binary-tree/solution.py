# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        
        # base case
        # the depth of a non-existent node is 0
        def dfs(current_node):
            if not current_node:
                return 0

            # get the depth of the left side of the tree
            left_depth = dfs(current_node.left)
            # get the depth of the right side of the tree
            right_depth = dfs(current_node.right)

            self.max_diameter = max(self.max_diameter, left_depth+right_depth)

            # take the maximum, and +1 for the current node
            return 1 + max(left_depth, right_depth)

        dfs(root)
        
        return self.max_diameter

        
