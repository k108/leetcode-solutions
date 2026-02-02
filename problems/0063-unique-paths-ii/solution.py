class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.approach_4(obstacleGrid)

    def approach_4(self, obstacleGrid: List[List[int]]) -> int:
        '''
        Time Complexity : O(R * C)
        Space Complexity : O(C)
        '''
        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0

        R = len(obstacleGrid)
        C = len(obstacleGrid[0])

        dp = [0]*C
        dp[0] = 1

        for r in range(R):
            for c in range(C):
                if obstacleGrid[r][c] == 1:
                    dp[c] = 0
                else:
                    if c > 0:
                        dp[c] += dp[c - 1]

        return dp[C - 1] 

    def approach_3(self, obstacleGrid: List[List[int]]) -> int:
        '''
        Time Complexity : O(R * C)
        Space Complexity : O(C)
        '''
        '''
        Bottom-Up \ Iterative DP :-
        We just need to know the previous rows results
        We just need to know the previous column results
        Last row and last colum outside 
        them out of bounds can be thought of 0's

        dp[r][c] = number of unique paths from cell (r, c) to destination

        Transition:
            If obstacleGrid[r][c] == 1:
                dp[r][c] = 0
            Else:
                dp[r][c] = dp[r][c + 1] + dp[r + 1][c]

        We compute the DP table from bottom-right to top-left.
        Only the previous row is required at any time, so we use 1D arrays.
        '''
        R = len(obstacleGrid)
        C = len(obstacleGrid[0])

        # prev_row[c] represents dp[r+1][c] (the row below the current row)
        prev_row = [0] * C

        # Traverse rows from bottom to top
        for r in range(R -1, -1, -1):
            # curr_row[c] represents dp[r][c] for the current row
            curr_row = [0] * C

            # Handle last column,
            # The destination cell (R-1, C-1) is not always reachable
            # The last column is not always all 1s
            # Handle the last column separately because:
            # - There is no cell to the right
            # - The value only depends on the cell below
            # - The destination cell (R-1, C-1) is a special base case
            if obstacleGrid[r][C - 1] == 1:
                # Obstacle blocks all paths
                curr_row[C - 1] = 0
            else:
                if r == R - 1:
                    # Destination cell contributes exactly one valid path
                    # Destination cell
                    curr_row[C - 1] = 1
                else:
                    # Inherit paths from the cell directly below
                    curr_row[C - 1] = prev_row[C - 1]

            # Fill the rest of the row from right to left
            for c in range(C-2, -1, -1):
                if obstacleGrid[r][c] == 1:
                    # Obstacle blocks all paths through this cell
                    curr_row[c] = 0
                else:
                    # Sum of paths from:
                    # - Right neighbor (curr_row[c + 1])
                    # - Bottom neighbor (prev_row[c])
                    curr_row[c] = curr_row[c + 1] + prev_row[c]

            # Move current row up to become the "previous row" for next iteration
            prev_row = curr_row

        # Top-left cell contains the total number of unique paths
        return prev_row[0]

    def approach_2(self, obstacleGrid: List[List[int]]) -> int:
        '''
        Time Complexity : O(R * C)
        Space Complexity : O(R * C)
        '''
        R = len(obstacleGrid)
        C = len(obstacleGrid[0])

        dp = [[0]*C for i in range(R)]

        def dfs(r, c, R, C):
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
            dp[r][c] = dfs(r + 1, c, R, C) + dfs(r, c+1, R, C)
            return dp[r][c]

        ans = dfs(0, 0, R, C)

        return ans

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
