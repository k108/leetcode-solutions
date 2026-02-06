class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        return self.approach_3(stoneValue)

    def approach_3(self, stoneValue):
        '''
        Time Complexity : O(N) 
        Space Complexity : O(1)
        '''
        '''
        Approach : Bottom Up DP / Iterative DP

        We only need last 3 results: dp[i+1], dp[i+2] and dp[i+3]
        We depend on dp[i+1], dp[i+2], dp[i+3], hence we need a rolling buffer of size 4.

        Recurrence Relation :

        State Definition : 

        dp(i) = Maximum score difference (current player − other player),
        when starting from index i.

        Base case :

        dp[N] = 0, No stones left → no one scores anything

        Recurrence :
        From index 'i', the current player can take 1, 2, or 3 stones.

        If they take k stones:

        They gain: stoneValue[i] + ... + stoneValue[i + k - 1]

        Then, the opponent plays optimally from i + k, gaining dp[i + k]

        So the net advantage is:

        (sum of taken stones) − dp[i + k]

        dp[i] = max( sum(stoneValue[j]) - dp[i+k] ), k ∈ {1, 2, 3}, i+k <= N, j ∈ [i, i+k-1]

        dp[i] = max(
                    stoneValue[i] - dp[i + 1],
                    stoneValue[i] + stoneValue[i+1] - dp[i + 2],
                    stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp[i + 3],
                )

        Intuition :

        Boundary Condition :

        DP state Table :
	
        '''
        N = len(stoneValue)
        # dp[i % 4] represents dp[i]
        dp = [0] * 4
        
        for i in range(N-1, -1, -1):
            dp[i % 4] = float('-inf')
            take = 0

            for j in range(i, min(i + 3, N)):
                take += stoneValue[j]
                dp[i % 4] = max(
                    dp[i % 4], 
                    take - dp[(j + 1) % 4]
                )
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"

    def approach_2(self, stoneValue):
        '''
        Time Complexity : O(N) 
        Space Complexity : O(N), stack space
        '''
        '''
        Approach : DFS with Memoization / Top Down DP

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
