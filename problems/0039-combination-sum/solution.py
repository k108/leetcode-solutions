class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        '''
        Time Complexity : O( 2 ^ target )
        '''

        N = len(candidates)
        result = []

        def dfs(i, subset, total):
            # base case : reached end of array or 
            # total gets bigger than the target
            if i>=N or total > target:
                return

            # base case : total equals target
            if total == target:
                result.append(subset.copy())
                return

            # decision to add the element
            subset.append(candidates[i])
            dfs(i, subset, total + candidates[i])

            # decision to not add the element and use the next element
            subset.pop()
            dfs(i+1, subset, total)

        dfs(0, [], 0)

        return result

        
