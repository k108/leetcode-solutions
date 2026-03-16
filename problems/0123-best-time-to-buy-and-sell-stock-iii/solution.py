class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.approach_3(prices)

    def approach_3(self, prices: List[int]) -> int:
        '''
        Time Complexity : O(N)
        Space Complexity : O(1)
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

        # int[][][] dp = new int[3][2]
        next = [[0]*2 for _ in range(3)]

        for i in range(len(prices)-1, -1, -1):
            curr = [[0]*2 for _ in range(3)]
            for k in range(1, 3):

                # buy
                curr[k][0] = max(
                    -prices[i] + next[k][1], # buy
                    next[k][0] # skip
                )

                # sell
                curr[k][1] = max(
                    prices[i] + next[k-1][0], # sell
                    next[k][1] # skip
                )

            next = curr
        
        # start at day 0
        # 2 transactions available
        # not holding stock
        return next[2][0]

    def approach_2(self, prices: List[int]) -> int:
        '''
        Time Complexity : O(N)
        Space Complexity : O(N)
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

        # int[][][] dp = new int[n + 1][3][2]
        dp = [[[0]*2 for _ in range(3)] for _ in range(len(prices)+1)]

        for i in range(len(prices)-1, -1, -1):
            for k in range(1, 3):

                # buy
                dp[i][k][0] = max(
                    -prices[i] + dp[i+1][k][1],
                    dp[i+1][k][0]
                )

                # sell
                dp[i][k][1] = max(
                    prices[i] + dp[i+1][k-1][0],
                    dp[i+1][k][1]
                )

        return dp[0][2][0]

    def approach_1(self, prices: List[int]) -> int:
        '''
        Time Complexity : O(N)
        Space Complexity : O(N)
        '''
        '''
        Approach : DFS with memoization

        Buy -> hold -> Sell -> transaction completed
        '''

        @cache
        def dfs(day, holding, num_transactions):
            if day>=len(prices) or num_transactions == 2:
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
