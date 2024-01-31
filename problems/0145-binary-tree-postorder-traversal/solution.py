# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root == None:
            return

        visited = set()
        stack = []
        if root != None:
            stack.append(root)

        while len(stack)>0:
            node = stack.pop()
            if node in visited:
                result.append(node.val)
            else:
                visited.add(node)
                stack.append(node)
                if node.right != None:
                    stack.append(node.right)
                if node.left != None:
                    stack.append(node.left)
        return result

        
