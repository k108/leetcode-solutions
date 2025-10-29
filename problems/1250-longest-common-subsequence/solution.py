class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        Time Complexity : O(m * n)
        Space Complexity : O(m * n)
        '''
        '''
        DP[i][j] represents the longest common subsequence of text1[0 ... i] & text2[0 ... j]
        DP[i][j] = DP[i - 1][j - 1] + 1 , if text1[i] == text2[j] DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) , otherwise
        '''
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[-1][-1]
