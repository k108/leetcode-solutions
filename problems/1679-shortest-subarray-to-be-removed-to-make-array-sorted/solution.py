import bisect

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        '''
        Time Complexity : O(n * log n)
        Space Complexity : O(1)
        '''

        '''
        Approach :

        Look for any parts of the array that are already sorted and
        try to retain as much of that as possible

        Find the longest non-decreasing subarray
        starting with the first element ( prefix ) or
        ending with the last element ( suffix )

        After removing some subarray, the result is the concatenation of
        a sorted prefix and a sorted suffix, where the last element of 
        the prefix is smaller than the first element of the suffix.

        Use binary search to find the smallest index in the right part of the array
        where the element is greater than or equal to the last element ( largest index )
        of the left part
        i.e. find the smallest middle block of numbers to remove.
        '''
        n = len(arr)
        # Step 1 : Find the longest non-decreasing prefix
        prefix_index = 0
        while prefix_index+1<n and arr[prefix_index] <= arr[prefix_index+1]:
            prefix_index+=1
        
        # left array is sorted
        if prefix_index==n-1:
            return 0

        # Step 2 : Find the longest non-decreasing suffix
        suffix_index = n-1
        while suffix_index-1>=0 and arr[suffix_index-1] <= arr[suffix_index]:
            suffix_index-=1

        # Step 3 : Start with removing either left or right part completely
        ans = min(n - (prefix_index + 1), suffix_index)
    
        # Step 4 : Concat prefix and suffix, such as prefix[-1] <= suffix[0]
        for i in range(prefix_index, -1, -1):
            j = bisect.bisect_left(arr, arr[i], suffix_index, n)
            if j != -1:
                ans = min(ans, j-(i+1))
    
        return ans

# Test Cases
s = Solution()
assert 3 == s.findLengthOfShortestSubarray([9, 8, 7, 1, 2, 3])
assert 2 == s.findLengthOfShortestSubarray([1, 7, 8, 9, 2, 3])
assert 4 == s.findLengthOfShortestSubarray([1, 2, 2, 2, 1, 4, 5, 6, 3])
assert 3 == s.findLengthOfShortestSubarray([2, 2, 2, 1, 1, 1])
assert 8 == s.findLengthOfShortestSubarray([6, 3, 10, 11, 15, 20, 13, 3, 18, 12])
