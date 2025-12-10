from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Time Complexity : O(n)
        Space Complexity : O(k)
        '''
        '''
        We use monotonically decreasing Deque
        We keep indexes in deque
        Left most element is maximum and we remove it from left
        We insert from right, pop till curr > right most element
        '''
        if k == 1:
            return nums

        d = deque()
        ans = []

        for i in range(len(nums)):
            while d and nums[d[-1]] < nums[i]:
                d.pop()

            d.append(i)

            if d[0] == i-k:
                d.popleft()

            if i >= k-1:
                ans.append(nums[d[0]])

        return ans
