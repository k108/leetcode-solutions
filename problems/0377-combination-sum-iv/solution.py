class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.approach_2(nums, target)

    def approach_2(self, nums: List[int], target: int) -> int:
        '''
        Time Complexity : O(N * target), each unique target value is calculated once.
        For each calculation, we might iterate over all N numbers in nums.
        Space Complexity : O(target)
        '''
        '''
        Memoization
        '''
        nums.sort()
        dp = {}

        def dfs(target):
            if target in dp:
                return dp[target]

            if target == 0:
                return 1
            # Pruning
            # Given that nums is sorted, this means no combination can be formed
            # to achieve the current target. So, we immediately return 0, optimizing our recursion.
            if target < nums[0]:
                return 0
            
            result = 0

            for num in nums:
                if target >= num:
                    result += dfs(target - num)
            
            dp[target] = result
            return result

        return dfs(target)

    def approach_1(self, nums: List[int], target: int) -> int:
        '''
        Time Complexity : O(N^target)
        Space Complexity : O(target)
        '''
        nums.sort()

        def dfs(target):
            if target == 0:
                return 1
            # Pruning
            # Given that nums is sorted, this means no combination can be formed
            # to achieve the current target. So, we immediately return 0, optimizing our recursion.
            if target < nums[0]:
                return 0
            
            result = 0

            for num in nums:
                if target >= num:
                    result += dfs(target - num)
            
            return result

        return dfs(target)
