class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Time Complexity : O(log n)
        """
        # since we have to find any peak element,
        # we go in monotonically increasing direction
        # we check left and right elements to the middle element in binary search
        # if left element < middle element > right element then we return peak
        # else if left element < middle element < right element, we search in right direction
        # else if left element > middle element > right element, we search in left direction

        N = len(nums)
        low = 0
        high = N-1

        while(low<=high):
            mid = low+((high-low)//2)

            # right neighbour greater
            if mid<N-1 and nums[mid]<nums[mid+1]:
                low=mid+1
            # left neighbour greater
            elif mid>0 and nums[mid]<nums[mid-1]:
                high=mid-1
            else:
                return mid

