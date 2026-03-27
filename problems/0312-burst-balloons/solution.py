class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        return self.approach_2(nums)

    def approach_2(self, nums: List[int]) -> int:
        '''
        Time Complexity : O(n^3)
        Space Complexity : O(n^2)
        '''
        '''
        Approach : 2D DP & Interval DP
        '''
        nums = [1] + nums + [1]

        dp = [[0]*len(nums) for _ in range(len(nums))]

        # size = distance between left and right
        for size in range(2, len(nums)):
            for left in range(len(nums) - size):
                right = left + size

                result = 0

                for i in range(left+1, right):
                    coins = nums[left] * nums[i] * nums[right]
                    left_result = dp[left][i]
                    right_result = dp[i][right]
                    result = max(result, coins + left_result + right_result)
                
                dp[left][right] = result
        
        return dp[0][len(nums)-1]

    def approach_1(self, nums: List[int]) -> int:
        '''
        Time Complexity : O(n^3)
        Space Complexity : O(n^2)
        '''
        '''
        Approach : DFS + Memoization

        State :
        f(left, right) -> maximum coins that can be collected from (left, right)

        Recurrence :
        f(left, right) = for i in [left+1, right),
        max(coins + f(left, i) + f(i, right))
        '''
        nums = [1] + nums + [1]

        @cache
        def dfs(left, right):
            result = 0

            for i in range(left+1, right):
                coins = nums[left] * nums[i] * nums[right]
                left_result = dfs(left, i)
                right_result = dfs(i, right)
                result = max(result, coins + left_result + right_result)
            
            return result
        
        return dfs(0, len(nums)-1)
