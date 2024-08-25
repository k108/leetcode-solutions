class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]

        def helper(nums, start, end):
            rob_1 = 0
            rob_2 = 0

            for i in range(start, end):
                rob_i = max(rob_2+nums[i], rob_1)
                rob_2 = rob_1
                rob_1 = rob_i

            return rob_1

        return max(helper(nums, 0, N-1), helper(nums, 1, N))

        
