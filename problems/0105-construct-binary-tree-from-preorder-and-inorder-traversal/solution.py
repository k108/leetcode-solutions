# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        N = len(inorder)
        self.pre_index = 0

        self.inorder_map = {}
        # to store the indices of the elements in a dict
        # Time Complexity : O(n^2) -> O(n)
        for i in range(N):
            self.inorder_map[inorder[i]] = i

        def construct_bt(inorder, preorder, start_index, end_index, size):
            """
            Time Complexity : O(n)
            """

            # preorder has root for each level
            # inorder has left_sub_tree, root and right_sub_tree
            
            # base case
            if start_index > end_index or self.pre_index >= size:
                return None

            # subtree root index
            root_index = self.inorder_map[preorder[self.pre_index]]

            # create the subtree root Node
            root = TreeNode(preorder[self.pre_index])

            # increment the pre_index variable
            self.pre_index += 1

            # construct left subtree
            root.left = construct_bt(inorder,preorder,start_index,root_index-1,size)

            # construct right subtree
            root.right = construct_bt(inorder,preorder,root_index + 1,end_index,size)

            # return the root of the subtree.
            return root

        return construct_bt(inorder, preorder, 0, N-1, N)
        
