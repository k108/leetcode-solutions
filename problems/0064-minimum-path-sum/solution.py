class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        Time Complexity : O(R * C)
        Space Complexity : O(R * C)
        '''

        R = len(grid)
        C = len(grid[0])
        def dfs(r, c, R, C, dp):
            # reached right most corner or
            # reached bottom most corner and
            # went out of bounds
            if r == R or c == C:
                return float('inf')

            if dp[r][c] != float('inf'):
                return dp[r][c]


            # reached the destination i.e. (R-1, C-1)
            if r == R-1 and c == C-1:
                return grid[r][c]
            
            # move either down i.e r+1 or right i.e. c+1
            dp[r][c] = grid[r][c] + min(dfs(r + 1, c, R, C, dp),dfs(r, c+1, R, C, dp))
            return dp[r][c]

        return dfs(0, 0, R, C, [[float('inf')]*C for i in range(R)])
