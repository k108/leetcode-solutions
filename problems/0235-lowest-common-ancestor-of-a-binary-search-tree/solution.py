# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # There can be 3 cases :
        # 1. The 1 node is on left of BST and other one is on right -> it means that root is the LCA
        # 2. Smaller node is less than root -> it means both nodes are on the left, 
        # so we take root.left as root node and repeat step 1.
        # 3. Smaller node is greater than root -> it means both nodes are on the right, 
        # so we take root.right as root node and repeat step 1.
        if not root:
            return root

        if p.val > q.val:
            p, q = q, p

        if (p.val <= root.val and q.val >= root.val) or (p.val >= root.val and q.val <= root.val):
            return root
        elif p.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)


        
