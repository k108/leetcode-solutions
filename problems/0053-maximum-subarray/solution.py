class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Time Complexity : O(n)
        Space Complexity : O(1)
        '''
        '''
        DP :
        max_sum = max(max_sum, running_sum - min_sum)
        '''

        min_sum = 0
        max_sum = float('-inf')
        for running_sum in itertools.accumulate(nums):
            max_sum = max(max_sum, running_sum - min_sum)
            min_sum = min(min_sum, running_sum)
        return max_sum
