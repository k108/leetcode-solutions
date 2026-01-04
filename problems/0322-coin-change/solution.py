class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        Time Complexity : O(amount * N)
        Space Complexity : O(amount)
        '''
        def dfs(remaining, dp):
            if remaining == 0:
                return 0
            if remaining < 0:
                return float('inf')

            if remaining in dp:
                return dp[remaining]

            res = float('inf')
            for coin in coins:
                res = min(res, dfs(remaining - coin, dp) + 1)

            dp[remaining] = res
            return res

        ans = dfs(amount, {})
        return ans if ans != float('inf') else -1
