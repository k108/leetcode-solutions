class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Time Complexity : O(n * 4^n)
        """
        if not digits:
            return []

        keypad = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        N = len(digits)
        result = []
        subset = ''

        def dfs(i, subset):
            # base case
            if i >= N:
                result.append(subset[:])
                return

            for alphabet in keypad[digits[i]]:
                dfs(i+1, subset+alphabet)
        
        dfs(0, subset)
        return result


        
