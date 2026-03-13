class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.approach_2(prices)

    def approach_2(self, prices: List[int]) -> int:
        '''
        Time Complexity : O(N)
        Space Complexity : O(N)
        '''
        '''
        Approach : DFS + Memoizatiom
        '''
        dp = [[-1] * 2 for _ in range(len(prices) + 2)]

        def dfs(day, holding):
            if day>=len(prices):
                return 0

            ans = dp[day][holding]

            if ans != -1:
                return ans
            
            # no transaction this day
            ans_1 = dfs(day+1, holding)

            # doing the required transaction this day
            if holding:
                # sell
                ans_2 = prices[day] + dfs(day+1,False)
            else:
                # buy
                ans_2 = -prices[day] + dfs(day+1,True)
            
            ans = max(ans_1, ans_2)

            dp[day][holding] = ans

            return ans

        return dfs(0, False)

    def approach_1(self, prices: List[int]) -> int:
        '''
        Time Complexity : O(2^N)
        Space Complexity : O(N)
        '''
        '''
        Approach : DFS

        Recurrence Relation :

        State Definition:
        f(day,holding) = maximum profit starting from day

        holding = True -> we are holding a stock and must sell before buying again
        holding = False -> we are allowed to buy

        Base Case :

        f(day,holding) = 0, if day >= N

        Recurrence :

        If holding = False :

        Two options:

        Skip the day -> f(day+1,False)

        Buy the stock -> −prices[day] + f(day+1,True)

        So,

        f(day,False) = max(f(day+1,False), −prices[day] + f(day+1,True))

        If holding = True :

        Two options:

        Skip the day -> f(day+1,True)

        Sell the stock ->

        prices[day]+f(day+1,False)

        f(day,True) = max(f(day+1,True), prices[day] + f(day+1,False))

        Final Answer = f(0,1)
	​
        Because initially:

        Day = 0

        We are not holding anything
        '''
        def dfs(day, holding):
            if day>=len(prices):
                return 0
            
            # no transaction this day
            ans_1 = dfs(day+1, holding)

            # doing the required transaction this day
            if holding:
                # sell
                ans_2 = prices[day] + dfs(day+1,False)
            else:
                # buy
                ans_2 = -prices[day] + dfs(day+1,True)
            
            return max(ans_1, ans_2)

        return dfs(0, False)
