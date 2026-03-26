class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        return self.approach_1(piles)

    def approach_1(self, piles: List[int]) -> int:
        '''
        Time Complexity : O(n^3) and O(3^n) without memoization
        Space Complexity : O(n^2)
        '''
        '''
        Approach : DFS + Memoization

        Recurrence :

        State :
        f(i, M) = maximum stones current player can get from piles[i:] with current M

        Recurrence Relation :

        f(i, M) = max over X ∈ [1, 2M] of:
        total_taken_now + (remaining_stones - opponent_best)

        or,

        Let suffix[i] = sum(piles[i:]),

        f(i, M) = max(
                    suffix[i] - f(i + X, max(M, X))
                )

        We take: sum(piles[i : i+X])
        Remaining stones: suffix[i + X]
        Opponent will optimally get: f(i + X, max(M, X))

        Gain = total remaining - opponent gain
            = suffix[i] - f(i + X, max(M, X))

        Base case :

        f(i, M) = 0,  if i >= n
        No piles left -> no stones to take.
        '''
        
        suffix = [0] * len(piles)
        suffix[-1] = piles[-1]
        for i in range(len(piles)-2, -1, -1):
            suffix[i] = piles[i] + suffix[i+1]

        @cache
        def dfs(i, M):
            if i >= len(piles):
                return 0

            if 2*M >= len(piles) - i:
                # If we can take all remaining piles, we take them
                return suffix[i]

            max_stones = 0

            for X in range(1, 2*M + 1):
                if i + X > len(piles):
                    break

                max_stones = max(
                    max_stones, 
                    suffix[i] - dfs(i + X, max(M, X))
                )
            return max_stones

        return dfs(0, 1)
