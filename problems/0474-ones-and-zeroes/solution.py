class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        return self.approach_3(strs, m, n)

    def approach_3(self, strs: List[str], m: int, n: int) -> int:
        '''
        Time Complexity : O(len(strs)*(m*n))
        Space Complexity : O(m*n)
        '''
        '''
        Approach : Bottom-Up Iterative DP

        Recurrence Relation :

        State Definition :
        dp(i,j) = The maximum number of strings that can be formed using at most
        i zeros and j ones, where 0 <= i <= m, 0 <= j <= n

        Base Case :
        dp[0][0] = 0
        dp[i][j] = 0 initially for all i,j
        With zero strings processed,
        or with insufficient capacity,
        we can pick 0 strings.

        Recurrence :
        For each string s_k,

        let,
        count_0 = number of zeros in sk_k
        count_1 = number of ones in sk_k

        dp[i][j] = max(
            1 + dp[i - count_0][j - count_1], # take it (if capacity allows)
            dp[i][j] # skip the string
        )

        For all i >= count_0 and j >= count_1

        Boundary Conditions :

        i >= count_0, j >= count_1
        0 <= i <= m,0 <= j <= n
        '''
        # Base case
        dp = [[0] * (n + 1) for _ in range(m+1)]

        for s in strs:
            count_0 = s.count('0')
            count_1 = s.count('1')
            for i in range(m, count_0 - 1, -1):
                for j in range(n, count_1 - 1, -1):
                    dp[i][j] = max(1 + dp[i - count_0][j- count_1], dp[i][j])
    
        return dp[-1][-1]

    def approach_2(self, strs: List[str], m: int, n: int) -> int:
        '''
        Time Complexity : O(len(strs)*(m*n))
        Space Complexity : O(m*n)
        '''
        '''
        Appoach : Memoization / Knapsack 0/1
        Capacity : At most m 0's and n 1's
        Weight : m 0's and n 1's
        Profit : largest subset
        '''
        @cache
        def dfs(i, capacity):
            if i == len(strs):
                return 0

            # Skip item i
            max_profit = dfs(i + 1, capacity)

            # Include item i
            new_capacity = (capacity[0] - strs[i].count('0'), capacity[1] - strs[i].count('1'))
            if new_capacity[0] >= 0 and new_capacity[1] >= 0:
                p = 1 + dfs(i + 1, new_capacity)
                # Compute the max
                max_profit = max(max_profit, p)

            return max_profit
        
        return dfs(0, (m,n))

    def approach_1(self, strs: List[str], m: int, n: int) -> int:
        '''
        Time Complexity : O(2^n)
        Space Complexity : O(n)
        '''
        '''
        Appoach : DFS / Knapsack 0/1
        Capacity : at most m 0's and n 1's
        Weight : m 0's and n 1's
        Profit : largest subset
        '''
        def dfs(i, capacity):
            if i == len(strs):
                return 0

            # Skip item i
            max_profit = dfs(i + 1, capacity)

            # Include item i
            new_capacity = (capacity[0] - strs[i].count('0'), capacity[1] - strs[i].count('1'))
            if new_capacity[0] >= 0 and new_capacity[1] >= 0:
                p = 1 + dfs(i + 1, new_capacity)
                # Compute the max
                max_profit = max(max_profit, p)

            return max_profit
        
        return dfs(0, (m,n))
