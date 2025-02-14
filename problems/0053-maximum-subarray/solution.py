class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Time Complexity : O(n)

        Space Complexity : O(1)
        '''

        '''
        Kadane’s Algorithm :
        It calculates the maximum sum subarray ending at a particular position 
        by using the maximum sum subarray ending at the previous position.
        '''
        # stores maximum sum so far
        max_sum = nums[0]
        # stores maximum sum ending here
        curr_sum = 0

        for n in nums:
            curr_sum+=n
            max_sum = max(max_sum, curr_sum)
            curr_sum = max(curr_sum, 0)

        return max_sum

        
