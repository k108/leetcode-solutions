class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Time Complexity : O(n)
        Space Complexity : O(1)
        '''
        '''
        one pointer to the current number and,
        another pointer to the place where the replacement should occur
        '''
        
        i = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1
        
        return i 
