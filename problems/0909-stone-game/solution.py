class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return self.approach_2(piles)

    def approach_4(self, piles: List[int]) -> bool:
        '''
        Time Complexity : O(1)
        Space Complexity : O(1)
        '''
        '''
        Approach : Mathematical

        There are an even number of piles
        The total number of stones across all the piles is odd

        Let 1, 3, 5, 7, etc. odd piles are white, and 
        the 2, 4, 6, 8, etc. even piles are black. 
        Alice (first player) can always take either all white piles or
        all black piles, and one of the colors must have a sum 
        number of stones larger than the other color.
        '''
        return True

    def approach_3(self, piles: List[int]) -> bool:
        '''
        Time Complexity : O(n^2)
        Space Complexity : O(n)
        '''
        '''
        Approach : Minimax + 1D DP

        dp[l][r] depends on:
        dp[l+1][r]   (next row, same column)
        dp[l][r-1]   (same row, previous column)

        State :
        dp[r] = represents dp[l][r] for current l

        dp[r] -> dp[l+1][r]   (old value, from previous l)
        dp[r-1] -> dp[l][r-1]   (already updated in current l loop)

        Reuse dp[r] as the next row and dp[r-1] as the current row 
        by updating from left to right while moving l backward.
        '''
        dp = [0]*len(piles)

        for l in range(len(piles)-1, -1, -1):
            for r in range(l, len(piles)):
                if l == r:
                    dp[r] = piles[l]
                else:
                    dp[r] = max(
                                piles[l] - dp[r],        # dp[l+1][r]
                                piles[r] - dp[r-1]       # dp[l][r-1]
                            )
        return dp[len(piles) - 1] > 0

    def approach_2(self, piles: List[int]) -> bool:
        '''
        Time Complexity : O(n^2) and O(2^n) without memoization
        Space Complexity : O(n^2)
        '''
        '''
        Approach : Minimax + 2D DP

        dp[l][r] depends on:
        dp[l+1][r]   (below)
        dp[l][r-1]   (left)
        '''
        dp = [[0]*len(piles) for _ in range(len(piles))]

        for l in range(len(piles)-1, -1, -1):
            for r in range(l, len(piles)):

                if l == r:
                    dp[l][r] = piles[l]
                else:
                    # choose from start
                    # gain - opponent's turn
                    choose_left = piles[l] - dp[l+1][r]

                    # choose from end
                    # gain - opponent's turn
                    choose_right = piles[r] - dp[l][r-1]

                    dp[l][r] = max(choose_left, choose_right)

        return dp[0][len(piles) - 1] > 0

    def approach_1(self, piles: List[int]) -> bool:
        '''
        Time Complexity : O(n^2) and O(2^n) without memoization
        Space Complexity : O(n^2)
        '''
        '''
        Approach : Minimax + DFS + Memoization

        Player chooses the move that maximizes their score difference over the opponent

        Recurrence :

        State :
        f(i, j) = maximum score difference current player can achieve over opponent

        Recurrence Relation :
        f(i, j) = max(
                        piles[i] - f(i+1, j),
                        piles[j] - f(i, j-1)
                    )

        Base case :
        f(i, i) = piles[i]
        If only one pile left then, current player takes it.

        Ans = Alice wins if f(0, n-1) > 0
        '''

        @cache
        def dfs(l, r):
            if l == r:
                return piles[l]

            # choose from start
            # gain - opponent's turn
            choose_left = piles[l] - dfs(l+1, r)

            # choose from end
            # gain - opponent's turn
            choose_right = piles[r] - dfs(l, r-1)

            return max(choose_left, choose_right)

        return dfs(0, len(piles) - 1) > 0
