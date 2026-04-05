class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        return self.approach_1(matrix)

    def approach_1(self, matrix: List[List[str]]) -> int:
        '''
        Time Complexity : O(R*C)
        Space Complexity : O(R*C)
        '''
        '''
        Pick any cell with value 1
        What is the largest square we can build ending here?

        f(i, j) = min(top, left, diag) + 1
        '''

        R = len(matrix)
        C = len(matrix[0])

        @cache
        def dfs(r, c):

            if r < 0 or c < 0:
                return 0

            if matrix[r][c] == '1':
                return min(dfs(r, c-1), dfs(r-1, c), dfs(r-1, c-1)) + 1

            return 0

        max_side = 0
        for i in range(R):
            for j in range(C):
                max_side = max(max_side, dfs(i, j))

        return max_side ** 2
