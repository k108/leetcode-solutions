class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        def dfs(path, used):
            if len(path) == len(nums):
                res.append(path.copy())
                return

            for i, digit in enumerate(nums):
                # skip used letters
                if used[i]:
                    continue

                # add letter to permutation, mark letter as used
                path.append(digit)
                used[i] = True
                dfs(path, used)

                # remove letter from permutation, mark letter as unused
                path.pop()
                used[i] = False

        res = []
        dfs([], [False]*len(nums))
        return res


        
