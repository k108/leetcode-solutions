class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        return self.approach_2(matrix)

    def approach_2(self, matrix: List[List[int]]) -> int:
        '''
        Time Complexity : O(R*C)
        Space Complexity : O(1)
        '''
        '''
        Approach : Iterative DP
        '''

        R, C = len(matrix), len(matrix[0])

        for r in range(1, R):
            for c in range(C):
                matrix[r][c] += min(
                    matrix[r-1][k] for k in (c - 1, c, c + 1) if 0 <= k < R
                    )
        
        return min(matrix[-1])

    def approach_1(self, matrix: List[List[int]]) -> int:
        '''
        Time Complexity : O(R*C)
        Space Complexity : O(R*C)
        '''
        '''
        Approach : DFS + Memoization

        f(r, c) = Minimum path sum that ends at (r, c)

        Answer = best among all endpoints in last row
        '''

        R = len(matrix)
        C = len(matrix[0])

        @cache
        def dfs(r, c):
            if c < 0 or c >= C:
                return float('inf')
            
            if r == 0:
                return matrix[r][c]

            return matrix[r][c] + min(
                dfs(r-1, c-1), 
                dfs(r-1, c), 
                dfs(r-1, c+1)
            )

        return min(dfs(R-1, c) for c in range(C))
