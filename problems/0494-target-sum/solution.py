class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.approach_5(nums, target)

    def approach_5(self, nums: List[int], target: int) -> int:
        '''
        Time Complexity : O(N * S)
        Space Complexity : O(S)
        '''
        '''
        Approach : 1D Knapsack / Bottom Up

        Each row in the 2D DP table only depends on the previous row.
        Once we have calculated the values for dp[index - 1], 
        we no longer need the values from dp[index - 2] or any earlier rows. 
        Thus, instead of maintaining a full 2D table, 
        we update a single array as we process each number in the list.

        For i = 1,
        dp[nums[i] + total_sum] = 1
        dp[-nums[i] + total_sum] = 1

        For each subsequent number, we create a new array and update it based on the previous array.
        This avoids the need to store the entire 2D table. For each possible sum, 
        we update the new array by adding the number of ways to reach that sum 
        by either adding or subtracting the current number.

        If the previous sum was 0 (i.e., dp[0 + totalSum] = 1), we can reach a sum of 1 
        by adding the current number (0 + 1 = 1) or a sum of -1 
        by subtracting the current number (0 - 1 = -1).

        dp[target + totalSum] -> Answer
        '''
        total_sum = sum(nums)
        dp = [0] * (2 * total_sum + 1)

        # Initialize the first row of the DP table
        dp[nums[0] + total_sum] = 1  # Adding nums[0]
        dp[-nums[0] + total_sum] += 1  # Subtracting nums[0]

        for index in range(1, len(nums)):
            next_dp = [0] * (2 * total_sum + 1)
            for sum_val in range(-total_sum, total_sum + 1):
                if dp[sum_val + total_sum] > 0:
                    next_dp[sum_val + nums[index] + total_sum] += dp[
                        sum_val + total_sum
                    ]
                    next_dp[sum_val - nums[index] + total_sum] += dp[
                        sum_val + total_sum
                    ]
            dp = next_dp

        # Return the result if the target is within the valid range
        return 0 if abs(target) > total_sum else dp[target + total_sum]

    def approach_4(self, nums: List[int], target: int) -> int:
        '''
        Time Complexity : O(N * S)
        Space Complexity : O(S)
        '''
        '''
        Approach : Subset Sum DP / 1D Knapsack Counting / Top Down

        Original Problem : sum(+-nums[i]) - target

        Let:
        P = numbers assigned +
        N = numbers assigned -

        Then: 
        sum(P) - sum(N) = target
        sum(P) + sum(N) = total_sum
        => 2P = target + total_sum
        P = (target + total_sum) / 2

        Therefore, count subsets whose sum = (target + total_sum) / 2

        If abs(target) > total_sum -> return 0
        If (target + total_sum) is odd -> return 0
        (because S must be integer)

        Intitition :
        Choosing which elements are positive automatically determines which are negative.
        So counting sign assignments
        = counting subsets P with required sum.

        Recurrence Relation :

        State Definition :
        dp[i][s]=number of ways to obtain sum s using first i elements 
        Where:
        i∈[0,n]
        s∈[0,S]

        Base Case :
        dp[0][0] = 1(There is exactly 1 way to make sum 0 using 0 elements — choose nothing.)

        dp[0][s] = 0 for s>0

        Recurrence :

        For i >= 1:
        If nums[i−1] <= s:
        dp[i][s] = dp[i−1][s] ( Do not take element nums[i−1] )
                    + dp[i−1][s − nums[i−1]] ( Take element nums[i−1] )
        Else:
        dp[i][s] = dp[i−1][s]

        dp[N][S] -> Answer

        '''
        total_sum = sum(nums)

        if abs(target) > total_sum:
            return 0
        if (target + total_sum) % 2 != 0:
            return 0

        subset_sum = (target + total_sum) // 2

        # dp[s] = number of ways to make sum s
        dp = [0] * (subset_sum + 1)
        dp[0] = 1 # one way to make sum 0 (empty subset)

        for num in nums: 
            # iterate backwards (0/1 knapsack style) 
            for s in range(subset_sum, num - 1, -1): 
                dp[s] += dp[s - num]

        return dp[subset_sum]

    def approach_3(self, nums: List[int], target: int) -> int:
        '''
        Time Complexity : O(N * S)
        Space Complexity : O(N * S)
        '''
        '''
        Approach : Iterative 2-D DP / Bottom - Up
        '''
        '''
        Recurrence Relation :

        State Definition :

        dp[i][s]=number of ways to obtain sum s using the first i+1 elements
        Where:
        i∈[0,n−1]
        s∈[−T,T]
        T= ∑nums[k], for k=0 to n−1

        Base Case :

        For the first element nums[0]:

        dp[0][nums[0]]+=1
        dp[0][−nums[0]]+=1

        If nums[0]=0, this correctly results in:
        
        dp[0][0]=2

        (because +0 and −0 are distinct choices)

        Recurrence :

        dp[i][s] = dp[i−1][s−nums[i]] + dp[i−1][s+nums[i]], For i ≥ 1

        '''
        total_sum = sum(nums)
        dp = [[0] * (2 * total_sum + 1) for _ in range(len(nums))]

        # Initialize the first row of the DP table
        dp[0][nums[0] + total_sum] = 1
        dp[0][-nums[0] + total_sum] += 1

        for index in range(1, len(nums)):
            for sum_val in range(-total_sum, total_sum + 1):
                if dp[index - 1][sum_val + total_sum] > 0:
                    dp[index][sum_val + nums[index] + total_sum] += dp[
                        index - 1
                    ][sum_val + total_sum]
                    dp[index][sum_val - nums[index] + total_sum] += dp[
                        index - 1
                    ][sum_val + total_sum]

        return (
            0
            if abs(target) > total_sum
            else dp[len(nums) - 1][target + total_sum]
        )

    def approach_2(self, nums: List[int], target: int) -> int:
        '''
        Time Complexity : O(N * S)
        Space Complexity : O(N * S)
        '''
        '''
        Approach : DFS + Memoization / Top-down DP
        '''
        N = len(nums)
        dp = [[-1] * (1000 + 1) for _ in range(20 + 1)]

        def dfs(i, target_sum):
            if i == N:
                if target_sum == target:
                    return 1
                else:
                    return 0

            if dp[i][target_sum] != -1:
                return dp[i][target_sum]

            result = dfs(i+1, target_sum + nums[i]) + dfs(i+1, target_sum - nums[i])

            dp[i][target_sum] = result
            return result
        
        return dfs(0, 0)   

    def approach_1(self, nums: List[int], target: int) -> int:
        '''
        Time Complexity : O(2^N)
        Space Complexity : O(N), recursion stack
        '''
        '''
        Approach : Brute-force DFS / Exhaustive search (± sign assignment)

        For every stone, choose + or - and compute the final target sum. 
        Try all 2^N possibilities and take the minimum valid result.

        For every element we have 2 choices, whether to give it "+" sign or "-" sign,
        as we can either add that elemnt or subtract it.
        Then we find out by which path we get the answer
        '''
        N = len(nums)

        def dfs(i, target_sum):
            if i == N:
                if target_sum == target:
                    return 1
                else:
                    return 0
            return dfs(i+1, target_sum + nums[i]) + dfs(i+1, target_sum - nums[i])
        
        return dfs(0, 0)    
