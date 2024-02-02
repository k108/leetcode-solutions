# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result_negative = []
        self.len_result_negative=0
        self.result_zero = []
        self.result_positive = []
        self.len_result_positive=0

        def dfs(root, row, col):
            if not root:
                return

            if col>0:
                if self.len_result_positive<=col-1:
                    self.len_result_positive+=1
                    self.result_positive.append([])
                #print(col-1)
                self.result_positive[col-1].append((root.val,row))
            elif col<0:
                if self.len_result_negative<=abs(col)-1:
                    self.len_result_negative+=1
                    self.result_negative.append([])
                #print(abs(col)-1)
                self.result_negative[abs(col)-1].append((root.val,row))
            else:
                self.result_zero.append((root.val,row))


            dfs(root.left, row+1, col-1)
            dfs(root.right, row+1, col+1)

        dfs(root, 0, 0)

        for idx in range(self.len_result_positive):
            self.result_positive[idx] = sorted(self.result_positive[idx], key=lambda x: (x[1], x[0]))
            self.result_positive[idx] = [e[0] for e in self.result_positive[idx]]

        for idx in range(self.len_result_negative):
            self.result_negative[idx] = sorted(self.result_negative[idx], key=lambda x: (x[1], x[0]))
            self.result_negative[idx] = [e[0] for e in self.result_negative[idx]]

        self.result_zero = sorted(self.result_zero, key=lambda x: (x[1], x[0]))
        self.result_zero = [e[0] for e in self.result_zero]

        return self.result_negative[::-1] + [self.result_zero] + self.result_positive

        
