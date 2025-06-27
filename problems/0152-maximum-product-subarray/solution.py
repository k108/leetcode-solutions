class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        Time Complexity : O(n)

        Space Complexity : O(1)
        '''

        '''
        Kadane’s Algorithm :
        It calculates the maximum prod subarray ending at a particular position 
        by using the maximum prod subarray ending at the previous position.
        '''
        curr_max_prod = 1
        curr_min_prod = 1
        max_prod = nums[0]
        for n in nums:
            # multiplied by a negative makes big number smaller, small number bigger
            # so we redefine the extremums by swapping them
            if n<0:
                curr_max_prod, curr_min_prod = curr_min_prod, curr_max_prod

            # max/min product for the current number is either the current number itself
            # or the max/min by the previous number times the current one
            curr_max_prod = max(n, curr_max_prod*n)
            curr_min_prod = min(n, curr_min_prod*n)

            # the newly computed max value is a candidate for our global result
            max_prod = max(max_prod, curr_max_prod)
    
        return max_prod

# Test Cases :
# s = Solution()
# 24 == s.maxProduct(nums=[-2,3,-4])
