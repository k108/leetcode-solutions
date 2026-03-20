class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        return self.approach_1(k, prices)

    def approach_1(self, k: int, prices: List[int]) -> int:
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
        
