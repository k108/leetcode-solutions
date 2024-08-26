# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.ans = -1
        def in_order(root):
            if not root or k<0:
                return

            in_order(root.left)
            self.k-=1
            if self.k == 0:
                self.ans = root.val
            in_order(root.right)
        in_order(root)
        return self.ans

            
        
