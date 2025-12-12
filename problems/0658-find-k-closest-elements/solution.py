import bisect

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        Time Complexity : O(log n + k)
        Space Complexity : O(1)
        '''
        '''
        because the array is sorted, the closest elements will be near the position 
        where x would be if it were present in the array

        Two-Pointer : Find the closest element and Expand using two pointers
        '''

        right = bisect.bisect_left(arr, x)
        left = right - 1

        while k > 0:
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                left -= 1
            else:
                right += 1
            k -= 1

        return arr[left+1 : right]
