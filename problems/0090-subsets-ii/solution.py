class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        def dfs(i, subset):
            if i >= len(nums):
                result.append(subset.copy())
                return
            
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1, subset)

            # decision not to include nums[i]
            subset.pop()
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                i+=1
            dfs(i+1, subset)
        
        dfs(0, [])
        return result
        
