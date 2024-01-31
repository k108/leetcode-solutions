# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_width = 0
        if not root:
            return
        queue = []
        queue.append((root,1))
        while queue:
            left_index = queue[0][1]
            right_index = queue[-1][1]
            max_width = max(max_width, right_index - left_index + 1)
            for _ in range(len(queue)):
                node, index = queue.pop(0)
                if node.left:
                    queue.append((node.left, 2*index))
                if node.right:
                    queue.append((node.right, 2*index+1))

        return max_width


        
