class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        return self.approach_2(stoneValue)
    
    def approach_2(self, stoneValue):
        '''
        Time Complexity : O(N) 
        Space Complexity : O(N), stack space
        '''
        '''
        Approach : DFS with Memoization

        minimax(i) : Maximum score difference (current player − other player) starting at index 'i'

        MaximizingPlayer is unnecessary here,
        This problem is zero-sum. You don’t need explicit min/max players.
        Instead, at position 'i', the current player chooses the move that maximizes score difference
        The opponent's optimal play is already baked into the recursive subtraction

        At every position i, how much better can the current player do
        than the other player from here on?
        That number can be:
        positive -> current player is ahead
        negative -> current player is behind
        zero -> tie
        i.e. score difference
        '''
        N = len(stoneValue)
        dp = [float('-inf')] * N

        def dfs(i):
            if i == N:
                return 0

            if dp[i] != float('-inf'):
                return dp[i]
            best = float('-inf')
            take = 0

            # Children = possible next moves (i+1, i+2, i+3)
            for j in range(i, min(i + 3, N)):
                take += stoneValue[j]
                # take = stones current player collects
                # minimax(j+1), opponent's best response
                best = max(best, take - dfs(j + 1))

            dp[i] = best
            return best

        score = dfs(0)

        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"

    def approach_1(self, stoneValue):
        '''
        Time Complexity : O(3^N) 
        Space Complexity : O(N), stack space
        '''
        '''
        Approach : DFS

        minimax(i) : Maximum score difference (current player − other player) starting at index 'i'

        MaximizingPlayer is unnecessary here,
        This problem is zero-sum. You don’t need explicit min/max players.
        Instead, at position 'i', the current player chooses the move that maximizes score difference
        The opponent's optimal play is already baked into the recursive subtraction

        At every position i, how much better can the current player do
        than the other player from here on?
        That number can be:
        positive -> current player is ahead
        negative -> current player is behind
        zero -> tie
        i.e. score difference
        '''
        N = len(stoneValue)

        def dfs(i):
            if i == N:
                return 0

            best = float('-inf')
            take = 0

            # Children = possible next moves (i+1, i+2, i+3)
            for j in range(i, min(i + 3, N)):
                take += stoneValue[j]
                # take = stones current player collects
                # minimax(j+1), opponent's best response
                best = max(best, take - dfs(j + 1))

            return best

        score = dfs(0)

        if score > 0:
            return "Alice"
        elif score < 0:
            return "Bob"
        else:
            return "Tie"
