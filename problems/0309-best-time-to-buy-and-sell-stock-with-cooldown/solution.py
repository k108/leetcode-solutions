class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.approach_3(prices)

    def approach_3(self, prices: List[int]) -> int:
        '''
        Time Complexity : O(N)
        Space Complexity : O(N)
        '''
        '''
        Approach : Iterative DP
        '''
        dp = [[0] * 2 for _ in range(len(prices) + 2)]

        for day in range(len(prices) - 1, -1, -1):
            for buy in [False, True]:
                # no transaction this day
                ans_1 = dp[day+1][buy]

                # doing the required transaction this day
                if buy:
                    ans_2 = -prices[day] + dp[day+1][False]
                else:
                    ans_2 = prices[day] + dp[day+2][True]

                dp[day][buy] = max(ans_1, ans_2)

        return dp[0][True]

    def approach_2(self, prices: List[int]) -> int:
        '''
        Time Complexity : O(N)
        Space Complexity : O(N)
        '''
        '''
        Approach : DFS + Memoizatiom
        '''
        dp = [[-1] * 2 for _ in range(len(prices) + 2)]

        def dfs(day, buy):
            if day>=len(prices):
                return 0

            ans = dp[day][buy]

            if ans != -1:
                return ans
            
            # no transaction this day
            ans_1 = dfs(day+1, buy)

            # doing the required transaction this day
            if buy:
                ans_2 = -prices[day] + dfs(day+1,False)
            else:
                ans_2 = prices[day] + dfs(day+2,True)
            
            ans = max(ans_1, ans_2)

            dp[day][buy] = ans

            return ans

        return dfs(0, True)

    def approach_1(self, prices: List[int]) -> int:
        '''
        Time Complexity : O(2^N)
        Space Complexity : O(N)
        '''
        '''
        Approach : DFS

        Recurrence Relation :

        State Definition:
        f(day,buy) = maximum profit starting from day

        buy = 1 -> we are allowed to buy
        buy = 0 -> we are holding a stock and must sell before buying again

        Base Case :

        f(day,buy) = 0, if day >= N

        Recurrence :

        If buy = 1 :

        Two options:

        Skip the day -> f(day+1,1)

        Buy the stock -> −prices[day] + f(day+1,0)

        So,

        f(day,1) = max(f(day+1,1), −prices[day] + f(day+1,0))

        If buy = 0 :

        Two options:

        Skip the day -> f(day+1,0)

        Sell the stock (cooldown of 1 day → move to day+2) ->

        prices[day]+f(day+2,1)

        f(day,0) = max(f(day+1,0), prices[day] + f(day+2,1))

        Final Answer = f(0,1)
	​
        Because initially:

        Day = 0

        We are allowed to buy
        '''
        def dfs(day, buy):
            if day>=len(prices):
                return 0
            
            # no transaction this day
            ans_1 = dfs(day+1, buy)

            # doing the required transaction this day
            if buy:
                ans_2 = -prices[day] + dfs(day+1,False)
            else:
                ans_2 = prices[day] + dfs(day+2,True)
            
            return max(ans_1, ans_2)

        return dfs(0, True)
