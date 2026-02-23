class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.approach_4(amount, coins)

    def approach_4(self, amount: int, coins: List[int]) -> int:
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

        Recurrence :
        dp(i, A) = dp(i + 1, A) + dp(i, A − coins[i]​)
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
