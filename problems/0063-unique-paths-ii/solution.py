class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.approach_2(obstacleGrid)

    def approach_2(self, obstacleGrid: List[List[int]]) -> int:
        '''
        Time Complexity : O(R * C)
        Space Complexity : O(R * C)
        '''
        R = len(obstacleGrid)
        C = len(obstacleGrid[0])
        def dfs(r, c, R, C, dp):
            # reached right most corner or
            # reached bottom most corner and
            # went out of bounds
            if r == R or c == C:
                return 0

            if dp[r][c] > 0:
                return dp[r][c]

            # reached an obstacle
            if obstacleGrid[r][c] == 1:
                return 0

            # reached the destination i.e. (R-1, C-1)
            if r == R-1 and c == C-1:
                return 1
            
            # move either down i.e r+1 or right i.e. c+1
            dp[r][c] = dfs(r + 1, c, R, C, dp) + dfs(r, c+1, R, C, dp)
            return dp[r][c]

        return dfs(0, 0, R, C, [[0]*C for i in range(R)])

    def approach_1(self, obstacleGrid: List[List[int]]) -> int:
        '''
        Time Complexity : O(2 ^ (r + c))
        Space Complexity : O(r + c)
        '''
        R = len(obstacleGrid)
        C = len(obstacleGrid[0])
        def dfs(r, c, R, C):
            # reached right most corner or
            # reached bottom most corner and
            # went out of bounds
            if r == R or c == C:
                return 0
            
            # reached an obstacle
            if obstacleGrid[r][c] == 1:
                return 0

            # reached the destination i.e. (R-1, C-1)
            if r == R-1 and c == C-1:
                return 1
            
            # move either down i.e r+1 or right i.e. c+1
            return dfs(r + 1, c, R, C) + dfs(r, c+1, R, C)

        return dfs(0, 0, R, C)
