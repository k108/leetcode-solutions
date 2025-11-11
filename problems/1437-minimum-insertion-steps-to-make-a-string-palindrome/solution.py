class Solution:
    def minInsertions(self, s: str) -> int:
        '''
        If longest palindromic subsequence is x and the length of the string is n then, 
        answer is n - x, as we need n - x insertions to make the remaining characters also palindrome
        '''
        def lps(s):
            '''
            Time Complexity : O(n^2)
            Space Complexity : O(n^2)
            '''
            '''
            This problems can be reduced to finding the LCS between
            the original string and its reversed form
            '''
            dp = [[0] * (len(s) + 1) for _ in range(len(s) + 1)]
            for i in range(len(s)):
                for j in range(len(s)):
                    if s[i] == s[len(s) - 1 - j]:
                        dp[i + 1][j + 1] = dp[i][j] + 1
                    else:
                        dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
            return dp[-1][-1]

        return len(s) - lps(s)
