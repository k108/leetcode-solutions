class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.approach_1(prices)

    def approach_1(self, prices: List[int]) -> int:
        '''
        Time Complexity : O(N)
        Space Complexity : O(N)
        '''
        '''
        Approach : DFS with memoization
        '''

        @cache
        def dfs(day, holding, num_transactions):
            if day>=len(prices):
                return 0

            if num_transactions > 2:
                return 0
            
            # no transaction this day
            ans_1 = dfs(day+1, holding, num_transactions)

            # doing the required transaction this day
            if holding:
                # sell
                ans_2 = prices[day] + dfs(day+1,False, num_transactions)
            else:
                # buy
                ans_2 = -prices[day] + dfs(day+1,True, num_transactions+1)
            
            return max(ans_1, ans_2)

        return dfs(0, False, 0)
