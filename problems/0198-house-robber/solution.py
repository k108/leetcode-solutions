class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        # what is more profitable:
        # 1. robbery of current house + loot from houses before the previous
        # 2. loot from the previous house robbery and any loot captured before that
        # rob(i) = max( rob(i - 2) + currentHouseValue, rob(i - 1) )
        
        rob_1 = 0
        rob_2 = 0

        for num in nums:
            rob_i = max(rob_2+num, rob_1)
            rob_2 = rob_1
            rob_1 = rob_i

        return rob_1

        
