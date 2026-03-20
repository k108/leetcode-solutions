class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        return self.approach_1(prices, fee)

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
