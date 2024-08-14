class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        N = len(nums)
        nums.sort()
        
        for i in range(N):
            if i>0 and nums[i]==nums[i-1]:
                continue
            left = i+1
            right = N-1
            while left < right:
                estimate = nums[i]+nums[left]+nums[right]

                if estimate < 0:
                    left+=1
                elif estimate > 0:
                    right-=1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    left+=1

                    while left < right and nums[left]==nums[left-1]:
                        left+=1
        
        return result

