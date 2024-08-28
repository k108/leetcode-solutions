# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        Time Complexity : O(n^2)
        Space Complexity : O(n)
        """
        self.max_path_sum = float("-inf")

        def max_path_sum(root):
            if not root:
                return 0
            # when looking at left and right branches of a node
            # we only care about gain we can make
            gain_on_left = max(max_path_sum(root.left), 0)
            gain_on_right = max(max_path_sum(root.right), 0)

            # maximum path we can form involving current node as root
            current_max_path_sum = root.val + gain_on_left + gain_on_right
            self.max_path_sum = max(self.max_path_sum , current_max_path_sum)

            # we cannot just return current_max_path_sum,
            # we can only form a path involving the parent node as root
            # with either of branches
            # so we choose the max gain between the gain from left branch 
            # and the gain from right branch 
            return root.val + max(gain_on_left , gain_on_right)

        max_path_sum(root)
        return self.max_path_sum
        
