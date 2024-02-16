# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if root.val == key:
            if root.right and root.left:
                # it has both children
                
                # The minimum node in its right subtree is found using the find_min function
                min_val = self.find_min(root.right)
                # The value of the current node is replaced by the value of the minimum node found
                root.val = min_val.val
                # The minimum node is then recursively deleted from the right subtree
                root.right = self.deleteNode(root.right, min_val.val)
            else:
                # it has one child
                if root.left:
                    return root.left
                else:
                    return root.right
                
        elif root.val > key:
            if root.left:
                root.left = self.deleteNode(root.left, key)
        else:
            if root.right:
                root.right = self.deleteNode(root.right, key)
                
        return root 
        
    def find_min(self, root):
        if root.left:
            return self.find_min(root.left)
        else:
            return root

        
