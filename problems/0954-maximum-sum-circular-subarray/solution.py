class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        '''
        Time Complexity : O(n)

        Space Complexity : O(1)
        '''

        '''
        Kadane’s Algorithm :
        It calculates the maximum sum subarray ending at a particular position 
        by using the maximum sum subarray ending at the previous position.

        There are two cases :-
        Case 1: The first is that the subarray take only a middle part,
        and we know how to find the max subarray sum, using Kadane's Algorithm
        Case2: The second is that the subarray take a part of head array
        and a part of tail array. We can transfer this case to the first one.

        max subarray circular sum = max(the max subarray sum, the total sum - 
        the min subarray sum)

        Corner Case :
        If all numbers are negative, maxSum = max(A) and minSum = sum(A).
        In this case, max(maxSum, total - minSum) = 0, which means the sum of an empty subarray.
        According to the description, We need to return the max(A),
        instead of sum of am empty subarray.
        So we return the maxSum to handle this corner case.
        '''
        # stores maximum sum so far
        max_sum = nums[0]
        # stores maximum sum ending here
        curr_max_sum = 0

        # stores minumum sum so far
        min_sum = nums[0]
        # stores minimum sum ending here
        curr_min_sum = 0

        total_sum = 0

        for num in nums:
            curr_max_sum = max(num, curr_max_sum + num)
            max_sum = max(max_sum, curr_max_sum)

            curr_min_sum = min(num, curr_min_sum + num)
            min_sum = min(min_sum, curr_min_sum)
            
            total_sum += num
        return max(max_sum, total_sum - min_sum) if max_sum > 0 else max_sum

# Test Cases :
# s = Solution()
# assert -1 == s.maxSubarraySumCircular(nums=[-1, -2, -3])
