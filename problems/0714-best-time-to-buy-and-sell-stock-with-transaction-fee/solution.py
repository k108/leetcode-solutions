class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        return self.approach_2(prices, fee)

    def approach_2(self, prices: List[int], fee: int) -> int:
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
            hold[i-1] + price - fee      # sell today
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
                prev_hold + prices[i] - fee      # sell today
                )
        
        return not_hold

    def approach_1(self, prices: List[int], fee: int) -> int:
        '''
        Time Complexity : O(N)
        Space Complexity : O(N)
        '''
        '''
        Approach : DFS with memoization

        Buy -> hold -> Sell -> transaction completed
        '''

        @cache
        def dfs(day, holding):
            if day>=len(prices):
                return 0
            
            # no transaction this day
            ans_1 = dfs(day+1, holding)

            # doing the required transaction this day
            if holding:
                # sell
                ans_2 = prices[day] - fee + dfs(day+1,False)
            else:
                # buy
                ans_2 = -prices[day] + dfs(day+1,True)
            
            return max(ans_1, ans_2)

        return dfs(0, False)
