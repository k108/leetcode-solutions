# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root, subRoot):
        self.same_tree = True
        def dfs(current_node_1, current_node_2):
            if not current_node_1 and not current_node_2:
                return
            elif not current_node_1 and current_node_2:
                self.same_tree = False
                return
            elif not current_node_2 and current_node_1:
                self.same_tree = False
                return

            if current_node_1.val != current_node_2.val:
                self.same_tree = False

            dfs(current_node_1.left, current_node_2.left)
            dfs(current_node_1.right, current_node_2.right)

        dfs(root, subRoot)
        return self.same_tree

        
