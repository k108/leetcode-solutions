class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        Time Complexity : O(n * 2^n)
        '''
        N = len(nums)
        result = []
        subset = []

        def dfs(i):
            # base case
            if i >= N:
                result.append(subset.copy())
                return result

            # decision to include nums[i], left branch
            subset.append(nums[i])
            dfs(i+1)

            # decision NOT to include nums[i], right branch
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return result
        
