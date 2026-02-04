class Solution:
    def integerBreak(self, n: int) -> int:
        return self.approach_2(n)

    def approach_2(self, n: int) -> int:
        '''
        Time Complexity : O(n^2)
        Space Complexity : O(n) for call stack
        '''
        '''
        Approach: DFS with Memoization / Top-Down 

        For each split i + (n - i):
        - stop splitting: i * (n - i)
        - keep splitting: i * dfs(n - i)
        '''

        dp = [-1] * (n + 1)

        def dfs(n):
            if dp[n] != -1:
                return dp[n]

            if n == 1:
                return 1

            result = float('-inf')

            for i in range(1, n):
                result = max(result, i * dfs(n - i), i * (n - i))

            dp[n] = result
            return result
        
        return dfs(n)

    def approach_1(self, n: int) -> int:
        '''
        Time Complexity : O(2^n)
        Space Complexity : O(n) for call stack
        '''
        '''
        Approach: DFS

        For each split i + (n - i):
        - stop splitting: i * (n - i)
        - keep splitting: i * dfs(n - i)
        '''
        def dfs(n):
            if n == 1:
                return 1
            result = float('-inf')
            for i in range(1, n):
                result = max(result, i * dfs(n - i), i * (n - i))
            return result
        
        return dfs(n)
