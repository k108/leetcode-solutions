# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build_bst(arr, left, right):
            if left > right:
                return None
            else:
                mid = left + (right - left)//2 
                return TreeNode(val = arr[mid], left = build_bst(arr, left, mid - 1), right = build_bst(arr, mid + 1, right))
        return build_bst(nums, 0, len(nums)-1)
        
