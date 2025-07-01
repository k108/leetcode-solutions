class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        Time Complexity : O(n)
        Space Complexity : O(1)
        '''
        '''
        jump length is always positive

        everytime we move towards right, we loose 1 jump
        if our number of jumps < new number of jumps, we
        replace number of jumps with new number of jumps
        if we eventually run of of jumps then return false,
        else if we reach the end we return true
        '''
        N = len(nums)
        jumps =  nums[0]

        for n in nums:
            if jumps < 0:
                return False
            elif jumps < n:
                jumps = n
            jumps -=1

        return True
