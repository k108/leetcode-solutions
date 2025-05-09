class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        '''
        Time Complexity : O(n)
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

        We can optimize the solution further by replacing binary search (O(N * log N))
        with a more efficient two-pointer approach, reducing the complexity to O(N)

        arr[left-1] is the largest element in this sorted prefix
        arr[right] is the smallest element in the sorted suffix
        For the two sorted sections to form one valid sorted sequence when combined, 
        we need the largest element in the left portion (arr[left-1])
        to be less than or equal to the smallest element in the right portion (arr[right])

        Using this two-pointer method, for each position of left,
        we search for the smallest right where arr[left] <= arr[right].
        If this condition holds, then we have found a valid subarray candidate 
        to remove—the subarray between arr[left] and arr[right], 
        which has a length of right - left - 1. 
        If arr[left] > arr[right], we increment right to find the next possible match. 
        Once a valid right is found, we advance left to the next element, repeating the process.
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
        # Find the minimum length to remove by comparing prefix and suffix
        ans = min(n - (prefix_index + 1), suffix_index)
    
        # Step 4 : Concat prefix and suffix, such as prefix[-1] <= suffix[0]
        i = 0
        j = suffix_index
        
        while i <= prefix_index and j < n:
            if arr[i] <= arr[j]:
                ans = min(ans, j-(i+1))
                i += 1
            else:
                j += 1
    
        return ans


# Test Cases
s = Solution()
assert 3 == s.findLengthOfShortestSubarray([9, 8, 7, 1, 2, 3])
assert 2 == s.findLengthOfShortestSubarray([1, 7, 8, 9, 2, 3])
assert 4 == s.findLengthOfShortestSubarray([1, 2, 2, 2, 1, 4, 5, 6, 3])
assert 3 == s.findLengthOfShortestSubarray([2, 2, 2, 1, 1, 1])
assert 8 == s.findLengthOfShortestSubarray([6, 3, 10, 11, 15, 20, 13, 3, 18, 12])
