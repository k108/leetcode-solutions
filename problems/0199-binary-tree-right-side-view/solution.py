# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # After traversing each level we find the right most node 
        # and collect its value in the result list.

        result = []
        if root == None:
            return []
        
        queue = []
        queue.append(root)
        
        while(len(queue)):
            for _ in range(len(queue)):
                node = queue[0]
                queue.pop(0)
                
                if node.left:
                    queue.append(node.left)
                    
                if node.right:
                    queue.append(node.right)

            result.append(node.val)

        return result



        
