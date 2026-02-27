class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        return self.approach_5(days, costs)

    def approach_5(self, days: List[int], costs: List[int]) -> int:
        '''
        Time Complexity : O(D), where where D = last travel day
        Space Complexity : O(30) = O(1)
        '''
        '''
        Appoach : Prefix DP / Bottom-Up DP
        
        Since we only look 30 days back,
        we can just store the cost for last 30 days in a rolling array.

        Also we can only look at calendar days,
        within our first and last travel dates.
        '''
        start = days[0]
        end = days[-1]

        days = set(days)

        # dp[i] = min cost to cover up to day i
        dp = [0] * 30
        
        for i in range(start, end + 1):
            if i not in days:
                dp[i % 30] = dp[(i - 1) % 30]
            else:
                dp[i % 30] = min(
                    dp[(i - 1) % 30] + costs[0],
                    dp[(max(0, i - 7)) % 30] + costs[1],
                    dp[(max(0, i - 30)) % 30] + costs[2],
                )
        
        return dp[end % 30]

    def approach_4(self, days: List[int], costs: List[int]) -> int:
        '''
        Time Complexity : O(n), where n = 365
        Space Complexity : O(n), where n = 365
        '''
        '''
        Appoach : Prefix DP / Bottom-Up DP

        What is the minimum cost to reach today?

        State : 
        
        dp(i) = Minimum price to cover all travel days from day 1 to day i

        Base case:

        dp(0) = 0

        Recurrence :

        For each day i ∈ [1,365],

        If day 'i' is a travel day:

        dp(i) = min({ 
				oneDayPass + dp(max(0, i−1)),
				oneWeekPass + dp(max(0, i−7)),
				oneMonthPass + dp(max(0, i−30)) 
			})

        If not a travel day:

        dp(i) = dp(i-1)

        Answer : dp(365)

        '''
        days = set(days)

        # dp[i] = min cost to cover up to day i
        dp = [0] * 366
        
        for i in range(1, 366):
            if i not in days:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(
                    dp[i - 1] + costs[0],
                    dp[max(0, i - 7)] + costs[1],
                    dp[max(0, i - 30)] + costs[2],
                )
        
        return dp[365]

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
				oneMonthPass + expectThisMonth 
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

        What is the cost from today to future?

        State : 
        
        f(i) = Minimum price for the i to 365 of the days

        Recurrence :

        If day 'i' is a travel day:

        f(i) = min({ 
				oneDayPass + exceptToday,
				oneWeekPass + expectThisWeek,
				oneMonthPass + expectThisMonth 
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
