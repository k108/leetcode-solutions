class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        return self.approach_4(matrix)

    def approach_4(self, matrix: List[List[str]]) -> int:
        '''
        Time Complexity : O(R*C)
        Space Complexity : O(1)
        '''
        '''
        Approach : In-place DP

        Instead of a separate dp, reuse matrix.
        Overwrite matrix[i][j] with DP value.
        '''
        R = len(matrix)
        C = len(matrix[0])

        count_all_1_square = 0

        for r in range(R):
            for c in range(C):

                if matrix[r][c] > 0 and r > 0 and c > 0:
                    matrix[r][c] = min(
                        matrix[r-1][c],
                        matrix[r][c-1],
                        matrix[r-1][c-1]
                    ) + 1

                count_all_1_square += matrix[r][c]

        return count_all_1_square

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

        count_all_1_square = 0
        prev_diag = 0

        for r in range(1, R+1):
            prev_diag = 0
            for c in range(1, C+1):
                temp = dp[c]

                if matrix[r-1][c-1]:

                    dp[c] = min(
                        dp[c-1],   # left
                        dp[c],     # top
                        prev_diag  # diag
                    ) + 1

                    count_all_1_square += dp[c]
                else:
                    dp[c] = 0

                prev_diag = temp
        
        return count_all_1_square


    def approach_2(self, matrix: List[List[str]]) -> int:
        '''
        Time Complexity : O(R*C)
        Space Complexity : O(R*C)
        '''
        '''
        Approach : Bottom-up Iterative DP
        '''
        R = len(matrix)
        C = len(matrix[0])

        dp = [[0] * (C + 1) for _ in range(R + 1)]

        count_all_1_square = 0

        for r in range(R):
            for c in range(C):
                if matrix[r][c]:
                    dp[r + 1][c + 1] = (
                        min(dp[r][c + 1], dp[r + 1][c], dp[r][c]) + 1
                    )
                    count_all_1_square += dp[r + 1][c + 1]
        return count_all_1_square

    def approach_1(self, matrix: List[List[str]]) -> int:
        '''
        Time Complexity : O(R*C)
        Space Complexity : O(R*C)
        '''
        '''
        Approach : DFS + Memoization

        Pick any cell with value 1
        Can we build square matrix of all 1's ending here? (anywhere in the matrix)

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
            if r == 0 or c == 0:
                return matrix[r][c]

            if matrix[r][c] == 1:
                return min(dfs(r, c-1), dfs(r-1, c), dfs(r-1, c-1)) + 1
            
            return 0

        count_all_1_square = 0
        for i in range(R):
            for j in range(C):
                count_all_1_square += dfs(i, j)

        return count_all_1_square
