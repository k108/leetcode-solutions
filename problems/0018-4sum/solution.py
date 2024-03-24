class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        quad, result = [], []

        def k_sum(k, start, target):
            if k!=2:
                for i in range(start, len(nums)-k+1):
                    # skip duplicates
                    if i>start and nums[i] == nums[i-1]:
                        continue
                    quad.append(nums[i])
                    k_sum(k-1, i+1, target-nums[i])
                    quad.pop()
                return
            else:
                left=start
                right=len(nums)-1
                while left < right:
                    if nums[left]+nums[right]<target:
                        left+=1
                    elif nums[left]+nums[right]>target:
                        right-=1
                    else:
                        result.append(quad+[nums[left], nums[right]])
                        # skip duplicates
                        left+=1
                        while left < right and nums[left]==nums[left-1]:
                            left+=1
        k_sum(4, 0, target)
        return result




        
