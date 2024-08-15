class Solution:
    def findMin(self, nums: List[int]) -> int:

        def binary_search(nums, left, right, rot_min):
            if left>right:
                return rot_min
            middle = (left+right)//2
            guess = nums[middle]
            rot_min = min(rot_min, guess)
            if guess >= nums[0]:
                left=middle+1
                return binary_search(nums, left, right, rot_min)
            else:
                right=middle-1
                return binary_search(nums, left, right, rot_min)

        return binary_search(nums, 0, len(nums)-1, nums[0])



        
