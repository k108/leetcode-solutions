class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.approach_2(nums, target)

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
