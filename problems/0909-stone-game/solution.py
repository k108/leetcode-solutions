class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return self.approach_1(piles)

    def approach_1(self, piles: List[int]) -> bool:
        '''
        Time Complexity : O(n^2) and O(2^n) without memoization
        Space Complexity : O(n^2)
        '''
        '''
        Approach : Minimax + DFS

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
            choose_left = piles[l] - dfs(l+1, r)

            # choose from end
            choose_right = piles[r] - dfs(l, r-1)

            return max(choose_left, choose_right)

        return dfs(0, len(piles) - 1) > 0
