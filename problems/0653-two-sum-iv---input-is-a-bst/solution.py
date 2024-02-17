# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # Use inorder traversal to get sorted array
        if not root:
            return False

        self.sorted_arr = []

        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            self.sorted_arr.append(root.val)
            inorder(root.right)

        inorder(root)

        # Use two pointers to find if there is a pair of elements adding up to k.
        l = 0
        r = len(self.sorted_arr)-1

        while l<r:
            curr_sum = self.sorted_arr[l] + self.sorted_arr[r]
            if curr_sum == k:
                return True
            elif curr_sum < k:
                l += 1
            elif curr_sum > k:
                r -= 1
        return False
        

        
