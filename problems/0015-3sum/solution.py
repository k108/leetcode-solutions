class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        target = 0
        for i in range(0, len(nums)):
            # skip duplicates
            if i>0 and nums[i] == nums[i-1]:
                continue

            left=i+1
            right=len(nums)-1
            while left < right:
                if nums[left]+nums[right]<target - nums[i]:
                    left+=1
                elif nums[left]+nums[right]>target - nums[i]:
                    right-=1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # skip duplicates
                    left+=1
                    while left < right and nums[left]==nums[left-1]:
                        left+=1
        return result

