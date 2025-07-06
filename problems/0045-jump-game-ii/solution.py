class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        Time Complexity : O(n)
        Space Complexity : O(1)
        '''
        N = len(nums)

        if N <= 1: return 0
        
        l, r = 0, nums[0]
        count = 1

        while r < len(nums) - 1:
            count += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt

        return count
