# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Use DFS (Depth First Search) to traverse the tree, 
        # and constantly keep track of the current path maximum.
        self.s=0
        def dfs(root, path_max):
            if not root:
                return
            path_max = max(path_max, root.val)

            if root.val >= path_max:
                self.s += 1

            dfs(root.left, path_max)
            dfs(root.right, path_max)
        dfs(root, -(2^1000000000))
        return self.s
            

        
