class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        return self.approach_1(matrix)

    def approach_1(self, matrix: List[List[str]]) -> int:
        '''
        Time Complexity : O(R*C)
        Space Complexity : O(R*C)
        '''
        '''
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
