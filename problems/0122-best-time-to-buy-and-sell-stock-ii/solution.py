class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.approach_5(prices)

    def approach_6(self, prices: List[int]) -> int:
        '''
        Time Complexity : O(N)
        Space Complexity : O(1)
        '''
        '''
        Approach : State Machine

        State :
        NOT_HOLD -> we do not own stock (can buy)
        HOLD -> we own stock (can sell)

        State Transitions :
        NOT_HOLD -> HOLD      (buy stock)
        NOT_HOLD -> NOT_HOLD  (do nothing)
        HOLD -> NOT_HOLD      (sell stock)
        HOLD -> HOLD          (keep holding)

        State Definitions :
        hold[i] = max profit on day i while holding stock
        not_hold[i] = max profit on day i while not holding stock

        hold[i] = max(
            hold[i-1],             # keep holding
            not_hold[i-1] - price  # buy today
            )

        not_hold[i] = max(
            not_hold[i-1],         # do nothing
            hold[i-1] + price      # sell today
            )
        
        Initial State :
        hold = -prices[0] ( can only buy )
        not_hold = 0
        '''

        hold = -prices[0]
        not_hold = 0

        for i in range(1, len(prices)):
            prev_hold = hold
            hold = max(
                hold,             # keep holding
                not_hold - prices[i]  # buy today
                )

            not_hold = max(
                not_hold,         # do nothing
                prev_hold + prices[i]      # sell today
                )
        
        return not_hold

    def approach_5(self, prices: List[int]) -> int:
        '''
        Time Complexity : O(N)
        Space Complexity : O(1)
        '''
        '''
        Approach : Greedy

        Every increasing price difference contributes to profit, 
        and collecting all of them is always optimal.
        '''
        profit = 0
        for i in range(1, len(prices)):
            # if prices[i] > prices[i - 1]:
            #     profit += prices[i] - prices[i-1]
            profit += max(0, prices[i] - prices[i-1])
        
        return profit

    def approach_4(self, prices: List[int]) -> int:
        '''
        Time Complexity : O(N)
        Space Complexity : O(1)
        '''
        '''
        Approach : Iterative 1D-DP

        For each day, we only need,

        dp[day+1][False]	next day's buy state
        dp[day+1][True] next day's sell state

        next_buy = dp[day+1][False]
        next_sell = dp[day+1][True]
        '''

        # base case
        # beyond the last day profit is 0
        next_buy  = 0
        next_sell = 0

        for day in range(len(prices) - 1, -1, -1):
            # dp[day+1][holding] -> next_buy, next_sell

            # sell
            curr_sell = max(
                next_sell, # skip
                prices[day] + next_buy # buy
            )

            # buy
            curr_buy = max(
                next_buy, # skip
                -prices[day] + next_sell  # sell
            )

            next_buy = curr_buy
            next_sell = curr_sell

        return next_buy

    def approach_3(self, prices: List[int]) -> int:
        '''
        Time Complexity : O(N)
        Space Complexity : O(N)
        '''
        '''
        Approach : Iterative 2D-DP
        '''

        dp = [[0] * 2 for _ in range(len(prices) + 2)]

        for day in range(len(prices) - 1, -1, -1):
            for holding in [False, True]:
                # no transaction this day
                ans_1 = dp[day+1][holding]

                # doing the required transaction this day
                if holding:
                    # sell
                    ans_2 = prices[day] + dp[day+1][False]
                else:
                    # buy
                    ans_2 = -prices[day] + dp[day+1][True]
                
                dp[day][holding] = max(ans_1, ans_2)

        return dp[0][False]

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
