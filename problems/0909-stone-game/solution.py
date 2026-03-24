class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return self.approach_2(piles)

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

        for length in range(1, len(piles)+1):
            for l in range(len(piles) - length + 1):
                r = l + length - 1

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
