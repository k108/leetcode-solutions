class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        return self.approach_3(days, costs)

    def approach_3(self, days: List[int], costs: List[int]) -> int:
        '''
        Time Complexity : O(n), where n = 365
        Space Complexity : O(n), where n = 365
        '''
        '''
        Appoach : Unbounded Knapsack / Top Down - Iterative DP
        '''
        days = set(days)
        dp = [0]*367
        # dp[366] = 0 already

        for i in range(365, 0, -1):
            # Skip
            # not travelling today, go to next day
            # without buying any ticket
            if i not in days:
                dp[i] = dp[min(366, i+1)]
            else:
                # Include
                dp[i] = min(
                    costs[0] + dp[min(366, i+1)],
                    costs[1] + dp[min(366, i+7)],
                    costs[2] + dp[min(366, i+30)],
                )
        
        return dp[1]

    def approach_2(self, days: List[int], costs: List[int]) -> int:
        '''
        Time Complexity : O(n), where n = 365
        Space Complexity : O(n), where n = 365
        '''
        '''
        Appoach : Memoization / Unbounded Knapsack
        Capacity : days
        Weight : costs
        Profit : minimum cost

        State : 
        
        f(i) = Minimum price for the i to 365 of the days

        Recurrence :

        If day 'i' is a travel day:

        f(i) = min({ 
				oneDayPass + exceptToday,
				oneWeekPass + expectThisWeek,
				oneMonthPass, expectThisMonth 
			})

        If not a travel day:

        f(i) = f(i+1)
        '''

        def dfs(i):
            # reached end of year
            if i > 365:
                return 0

            if dp[i] != -1:
                return dp[i]
            
            # Skip
            # not travelling today, go to next day
            # without buying any ticket
            if i not in days:
                result = dfs(i+1)
                dp[i] = result
                return result

            # Include
            result = min(
                costs[0] + dfs(i+1),
                costs[1] + dfs(i+7),
                costs[2] + dfs(i+30),
            )
            dp[i] = result
            return result

        days = set(days)
        dp = [-1]*366
        
        return dfs(1)

    def approach_1(self, days: List[int], costs: List[int]) -> int:
        '''
        Time Complexity : O(3^n), where n = 365
        Space Complexity : O(n), where n = 365
        '''
        '''
        Appoach : DFS / Unbounded Knapsack
        Capacity : days
        Weight : costs
        Profit : minimum cost

        State : 
        
        f(i) = Minimum price for the i to 365 of the days

        Recurrence :

        If day 'i' is a travel day:

        f(i) = min({ 
				oneDayPass + exceptToday,
				oneWeekPass + expectThisWeek,
				oneMonthPass, expectThisMonth 
			})

        If not a travel day:

        f(i) = f(i+1)
        '''

        def dfs(i):
            # reahed end of year
            if i > 365:
                return 0
            
            # Skip
            # not travelling today, go to next day
            # without buying any ticket
            if i not in days:
                return dfs(i+1)

            # Include
            return min(
                costs[0] + dfs(i+1),
                costs[1] + dfs(i+7),
                costs[2] + dfs(i+30),
            )

        days = set(days)
        
        return dfs(1)
