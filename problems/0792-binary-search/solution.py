class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (right+left)//2
            guess = nums[mid]
            if guess == target:
                return mid
            elif guess<target:
                left=mid+1
            elif guess>target:
                right=mid-1

        return -1        
