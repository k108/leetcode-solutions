# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good_nodes_count = 0
        def dfs(current_node, current_max):
            if not current_node:
                return
            
            if current_node.val >= current_max:
                current_max = current_node.val
                self.good_nodes_count+=1
            
            dfs(current_node.left, current_max)
            dfs(current_node.right, current_max)
        
        dfs(root, -(2^1000000000))
        return self.good_nodes_count

        
