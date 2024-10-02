class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1

        while left <= right:
            mid = (left+right)//2
            guess = nums[mid]
            if guess == target:
                return mid
            elif guess > target:
                right = mid-1
            else:
                left = mid+1

        return left

        
