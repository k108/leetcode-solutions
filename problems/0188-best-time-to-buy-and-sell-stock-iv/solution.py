class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        return self.approach_3(k, prices)

    def approach_3(self, k: int, prices: List[int]) -> int:
        '''
        Time Complexity : O(N * K)
        Space Complexity : O(K)
        '''
        '''
        Approach : 1-D DP

        curr = dp[i]
        next = dp[i+1]

        State :

        next[k][0] ->

        Maximum profit starting from the next day when:
        k transactions left
        not holding stock

        next[k][1] ->

        Maximum profit starting from the next day when:
        k transactions left
        holding stock
        '''

        # int[][][] dp = new int[k+1][2]
        next = [[0]*2 for _ in range(k+1)]

        for i in range(len(prices)-1, -1, -1):
            curr = [[0]*2 for _ in range(k+1)]
            for t in range(1, k+1):

                # buy
                curr[t][0] = max(
                    -prices[i] + next[t][1], # buy
                    next[t][0] # skip
                )

                # sell
                curr[t][1] = max(
                    prices[i] + next[t-1][0], # sell
                    next[t][1] # skip
                )

            next = curr
        
        # start at day 0
        # 2 transactions available
        # not holding stock
        return next[k][0]

    def approach_2(self, k: int, prices: List[int]) -> int:
        '''
        Time Complexity : O(N * K)
        Space Complexity : O(N * K)
        '''
        '''
        Approach : Bottom Up DP / Tabulation

        State :
        dp[i][k][0]

        Maximum profit:
        starting at day i
        k transactions remaining
        not holding stock

        dp[i][k][1]

        Maximum profit:
        starting at day i
        k transactions remaining
        holding stock
        '''

        # int[][][] dp = new int[n + 1][k+1][2]
        dp = [[[0]*2 for _ in range(k+1)] for _ in range(len(prices)+1)]

        for i in range(len(prices)-1, -1, -1):
            for t in range(1, k+1):

                # buy
                dp[i][t][0] = max(
                    -prices[i] + dp[i+1][t][1],
                    dp[i+1][t][0]
                )

                # sell
                dp[i][t][1] = max(
                    prices[i] + dp[i+1][t-1][0],
                    dp[i+1][t][1]
                )

        return dp[0][k][0]

    def approach_1(self, k: int, prices: List[int]) -> int:
        '''
        Time Complexity : O(N * K)
        Space Complexity : O(N * K)
        '''
        '''
        Approach : DFS with memoization

        Buy -> hold -> Sell -> transaction completed
        '''

        @cache
        def dfs(day, holding, num_transactions):
            if day>=len(prices) or num_transactions == k:
                return 0
            
            # no transaction this day
            ans_1 = dfs(day+1, holding, num_transactions)

            # doing the required transaction this day
            if holding:
                # sell
                ans_2 = prices[day] + dfs(day+1,False, num_transactions + 1)
            else:
                # buy
                ans_2 = -prices[day] + dfs(day+1,True, num_transactions)
            
            return max(ans_1, ans_2)

        return dfs(0, False, 0)
        
