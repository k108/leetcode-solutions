class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.approach_5(amount, coins)

    def approach_5(self, amount: int, coins: List[int]) -> int:
        '''
        Time Complexity : O(amount * len(coins))
        Space Complexity : O(amount)
        '''
        '''
        Unbounded Knapsack and Bottom-Up 1D DP :

        We don't actually need 'i' dimension if we process coins one by one.
        When processing coin c, we are allowing:
        Ways that use coin c any number of times,
        but only after all smaller-index coins are already fixed.
        So combinations are built in lexicographic coin order.
        That prevents permutation double counting.

        For combinations (not permutations):

        Outer loop = coins
        Inner loop = amount increasing

        This ensures:
        Each combination counted once
        Order doesn't matter
        If reversed -> we count permutations.

        Recurrence Relation :

        State :
        f(A) = number of ways to make amount A

        Base Case:
        f(0) = 1

        Recurrence :
        Then for each coin:
        f(A) += f(A−c), for all A >= c
        '''
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = dp[i] + dp[i - c]
        return dp[amount]

    def approach_4(self, amount: int, coins: List[int]) -> int:
        '''
        Time Complexity : O(amount * len(coins))
        Space Complexity : O(amount * len(coins))
        '''
        '''
        Unbounded Knapsack and Bottom-Up 2D DP :
        profit = 1
        weight = denomination
        capacity = amount

        Recurrence Relation :

        State :
        f(i,A) = number of ways to make amount A using coins from index i -> N-1

        Base Case :
        f(i,0) = 1
        f(i,A) = 0, if A < 0
        f(N,A) = 0, if A > 0

        Recurrence :
        dp(i, A) = dp(i + 1, A) + dp(i, A − coins[i]​)

        i + 1 -> depends on larger index -> iterate i backward
        A - coin[i] -> depends on smaller index -> iterate A forward

        answer = f(0, A) # All coins available and Full amount
        '''
        N = len(coins)
        dp = [[0] * (amount + 1) for _ in range(N + 1)]

        # Base case: amount = 0 -> 1 way
        for i in range(N + 1):
            dp[i][0] = 1

        for i in range(N-1, -1, -1):
            for a in range(0, amount + 1):

                # Skip coin
                dp[i][a] = dp[i + 1][a]

                # Take coin (unbounded)
                if a - coins[i] >= 0:
                    dp[i][a] += dp[i][a - coins[i]]

        return dp[0][amount]

    def approach_3(self, amount: int, coins: List[int]) -> int:
        '''
        Time Complexity : O(amount * len(coins))
        Space Complexity : O(amount * len(coins))
        '''
        '''
        Unbounded Knapsack and Memoization :
        profit = 1
        weight = denomination
        capacity = amount

        Recurrence Relation :

        State :
        f(i,A) = number of ways to make amount A using coins from index i -> N-1

        Base Case :
        f(i,0) = 1
        f(i,A) = 0, if A < 0
        f(N,A) = 0, if A > 0

        Recurrence :
        f(i, A) = f(i + 1, A) + f(i, A − coins[i]​)

        '''
        N = len(coins)
        dp = [[-1] * (amount + 1) for _ in range(N)]

        def dfs(i, amount):
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            if i == len(coins):
                return 0

            if dp[i][amount] != -1:
                return dp[i][amount]

            # Skip item i
            ways = dfs(i + 1, amount)

            # Include item i
            new_amount = amount - coins[i]
            if new_amount >= 0:
                ways += dfs(i, new_amount)

            dp[i][amount] = ways

            return ways
        
        return dfs(0, amount)

    def approach_2(self, amount: int, coins: List[int]) -> int:
        '''
        Time Complexity : O(amount * len(coins))
        Space Complexity : O(amount * len(coins))
        '''
        '''
        Unbounded Knapsack and Memoization :
        profit = 1
        weight = denomination
        capacity = amount
        '''
        N = len(coins)

        @cache
        def dfs(i, amount):
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            if i == len(coins):
                return 0

            # Skip item i
            ways = dfs(i + 1, amount)

            # Include item i
            new_amount = amount - coins[i]
            if new_amount >= 0:
                ways += dfs(i, new_amount)

            return ways
        
        return dfs(0, amount)
    
    def approach_1(self, amount: int, coins: List[int]) -> int:
        '''
        Time Complexity : O(2^amount)
        Space Complexity : O(amount)
        '''
        '''
        Unbounded Knapsack :
        profit = 1
        weight = denomination
        capacity = amount
        '''

        def dfs(i, amount):
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            if i == len(coins):
                return 0

            # Skip item i
            ways = dfs(i + 1, amount)

            # Include item i
            new_amount = amount - coins[i]
            if new_amount >= 0:
                ways += dfs(i, new_amount)

            return ways
        
        return dfs(0, amount)
