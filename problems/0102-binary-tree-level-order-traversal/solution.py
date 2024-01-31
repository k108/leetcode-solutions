# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        depth = 0

        def dfs(root, depth):
            if root == None:
                return
            
            if len(result) <= depth:
                result.append([])
            
            result[depth].append(root.val)
            depth += 1

            dfs(root.left, depth)
            dfs(root.right, depth)

        dfs(root, depth)
        return result

        
