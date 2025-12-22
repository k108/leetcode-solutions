# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        '''
        Time Complexity : O(n)
        Space Complexity : O(h), Recursive stack space, where h is the height of the tree
        '''
        '''
        BST, inorder traversal produces a sorted sequence.
        If two nodes are swapped by mistake, the inorder traversal
        will show a violation of the increasing order.
        We can detect these two nodes during inorder traversal and
        swap their values back to fix the BST.

        The first voilation element is always larger than its next one,
        while the second voilation element is always smaller than its previous one

        There can be one or two violations depending on 
        whether the swapped nodes are adjacent or not
        '''
        self.first = self.second = self.prev = None

        def in_order(root):
            if not root:
                return
            in_order(root.left)
            # Do something
            # print(root.val)

            # if previous is set and there is a voilation
            if self.prev and self.prev.val > root.val:
                # The first voilation element is always larger than its next one
                if not self.first:
                    self.first = self.prev
                # The second voilation element is always smaller than its previous one
                self.second = root
            
            # assign previous
            self.prev = root
            in_order(root.right)
        
        in_order(root)
        self.first.val, self.second.val = self.second.val, self.first.val
