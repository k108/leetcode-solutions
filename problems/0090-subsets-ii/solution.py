class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        Time Complexity : O(n * 2^n)
        '''
        N = len(nums)
        nums.sort()
        result = []

        def dfs(i, subset):
            # base case
            if i >= N:
                result.append(subset.copy())
                return

            # decision to include nums[i], left branch
            subset.append(nums[i])
            dfs(i+1, subset)

            # decision NOT to include nums[i], right branch
            subset.pop()

            # skip already used element
            while i+1<N and nums[i+1]==nums[i]:
                i+=1

            dfs(i+1, subset)

        dfs(0, [])
        return result
            
        
