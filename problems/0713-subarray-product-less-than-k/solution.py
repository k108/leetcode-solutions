class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        Time Complexity : O(n), The algorithm iterates through the input array nums using a
        single for loop. Inside the loop, there are nested operations for shrinking the window,
        but since left is incremented a total number of n times during the whole array traversal,
        each element in the array is visited at most twice.
        
        The nested loop terminates when the product becomes less than k, and this can only happen
        at most n times total (once for each element). Therefore, the overall time complexity is
        2n.

        Space Complexity : O(1)
        '''
        '''
        Sliding Window Approach :
        - The values in the nums array are positive
        - Products are increasing function
        - Once the product becomes less than k, all possible subarrays formed by 
        selecting subsets of elements within the current window (from left to right)
        will also have a product strictly less than k

        - The idea is always keep an max_product_window less than k;
        - Every time shift window by adding a new number on the right(j),
        if the product is greater than k, then try to reduce numbers on the left(i),
        until the subarray product fit less than k again, (subarray could be empty);
        - Each step introduces x new subarrays, where x is the size of the current window 
        (j + 1 - i);
        example:
        for window (5, 2), when 6 is introduced, it add 3 new subarray: (5, (2, (6)))
        (6)
        (2, 6)
        (5, 2, 6)
        '''
        # Handle edge cases where k is 0 or 1 (no subarrays possible)
        if k <= 1:
            return 0
        
        N = len(nums)

        # Use two pointers to maintain a sliding window
        left, right, count = 0, 0, 0
        max_product_window = 1

        while right < N:
            # Expand the window by including the element at the right pointer
            max_product_window *= nums[right]

            # Shrink the window from the left while the product is greater than or equal to k
            while max_product_window >= k and left <= right:
                # Remove the element at the left pointer from the product
                max_product_window //= nums[left]
                left += 1

            # Update the total count by adding the number of valid subarrays 
            # with the current window size
            # right - left + 1 represents the current window size
            count += right - left + 1

            right += 1

        return count
