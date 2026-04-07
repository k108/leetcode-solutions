class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        return self.approach_3(matrix)

    def approach_3(self, matrix: List[List[str]]) -> int:
        '''
        Time Complexity : O(R*C)
        Space Complexity : O(C)
        '''
        '''
        Approach : 1D DP

        Let 'r' be constant,

        dp[r][c] -> dp[c]
        dp[r][c-1] -> dp[c-1]
        dp[r-1][c] -> dp[c]
        dp[r-1][c-1] -> prev_diag, as dp[c-1] diagonal is lost unless, we store it.
        
        dp[c-1] has already been overwritten to represent current row
        '''

        R = len(matrix)
        C = len(matrix[0])
        
        dp = [0] * (C + 1)

        max_side = 0
        prev_diag = 0

        for r in range(1, R+1):
            prev_diag = 0
            for c in range(1, C+1):
                temp = dp[c]

                if matrix[r-1][c-1] == '1':

                    dp[c] = min(
                        dp[c-1],   # left
                        dp[c],     # top
                        prev_diag  # diag
                    ) + 1

                    max_side = max(max_side, dp[c])
                else:
                    dp[c] = 0

                prev_diag = temp
        
        return max_side ** 2

    def approach_2(self, matrix: List[List[str]]) -> int:
        '''
        Time Complexity : O(R*C)
        Space Complexity : O(R*C)
        '''
        '''
        Approach : Iterative / Bottom-Up DP
        '''
        R = len(matrix)
        C = len(matrix[0])
        
        # Base-case : if r < 0 or c < 0: return 0
        # dp[0][*] = 0
        # dp[*][0] = 0
        dp = [[0] * (C + 1) for _ in range(R + 1)]

        max_side = 0

        for r in range(1, R+1):
            for c in range(1, C+1):
                if matrix[r-1][c-1] == '1':
                    dp[r][c] = min(
                        dp[r][c-1],     # left
                        dp[r-1][c],     # top
                        dp[r-1][c-1]    # diag
                    ) + 1

                    max_side = max(max_side, dp[r][c])
        
        return max_side ** 2

    def approach_1(self, matrix: List[List[str]]) -> int:
        '''
        Time Complexity : O(R*C)
        Space Complexity : O(R*C)
        '''
        '''
        Pick any cell with value 1
        What is the largest square we can build ending here? (anywhere in the matrix)

        f(i, j) = min(top, left, diag) + 1

        A square ending at (i, j) needs:
        - A square above
        - A square to the left
        - A square diagonally (to ensure interior is filled)

        The smallest of these limits how big your square can be

        We do not use single call to dfs(R-1, C-1) here because it assumes,
        that the largest square must end at the bottom-right cell, while for
        this problem it can be anywhere in the matrix

        Recurrence :

        State :
        f(i, j) = side length of the largest square ending at cell (i, j)

        Recurrence Relation :

        # cannot form any square ending here
        f(i,j) = 0, if matrix[i][j]=0

        f(i,j) = min(f(i−1,j), f(i,j−1), f(i−1,j−1))+1, if matrix[i][j]=1

        Base Case :

        For i == 0 OR j == 0,

        If the cell is '1':
        We cannot look up / left / diagonal
        So the largest square is just the cell itself:
        f(i, j) = 1
	​
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
