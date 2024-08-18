class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        '''
        Time Complexity : O( n * 2 ^ n )
        Space Complexity : O( n )
        '''

        N = len(candidates)
        candidates.sort()
        result = []

        def dfs(i, subset, total):

            # base case : total equals target
            if total == target:
                result.append(subset.copy())
                return

            # base case : reached end of array or 
            # total gets bigger than the target
            if i>=N or total > target:
                return

            # decision to include the element
            subset.append(candidates[i])
            dfs(i+1, subset, total + candidates[i])

            # decision to skip the element
            subset.pop()

            while i+1 < N and candidates[i+1] == candidates[i]:
                i+=1

            dfs(i+1, subset, total)

        dfs(0, [], 0)

        return result

        
        
