class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        return self.approach_1(matrix)

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
