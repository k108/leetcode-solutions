# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        depth = 0
        def bfs(root):
            if root == None:
                return
            
            queue = []
            queue.append(root)
            
            while(queue):
                for _ in range(len(queue)):
                    root = queue[0]
                    queue.pop(0)
                    
                    if root.left:
                        queue.append(root.left)
                        
                    if root.right:
                        queue.append(root.right)
                result.append(root.val)
            
            return result

        return bfs(root)
        

        
