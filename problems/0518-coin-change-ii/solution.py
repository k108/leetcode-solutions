class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        return self.approach_2(amount, coins)

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

        @cache
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
