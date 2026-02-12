class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.approach_3(nums, target)

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
