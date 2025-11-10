class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        '''
        Use longest common subsequence
        The result string should contain all characters of s1 and s2 discarding the common ones.
        -> S1+S2-LCS
        Because characters appearing in LCS are coming twice in the result. So count them only once.
        '''

        '''
        Time Complexity : O(m * n)
        Space Complexity : O(m * n)
        '''
        '''
        DP[i][j] represents the longest common subsequence of text1[0 ... i] & text2[0 ... j]
        DP[i][j] = DP[i - 1][j - 1] + 1 , if text1[i] == text2[j] DP[i][j] = max(DP[i - 1][j], DP[i][j - 1]) , otherwise
        '''

        # Build LCS DP table
        dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
        for i in range(len(str1)):
            for j in range(len(str2)):
                if str1[i] == str2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        # Reconstruct the SCS using backtracking
        result = []
        i, j = len(str1), len(str2)
        # LCS gives the characters that must appear in order in the final result
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                result.append(str1[i-1])  # Common char (LCS)
                i -= 1
                j -= 1
            elif dp[i-1][j] >= dp[i][j-1]:
                result.append(str1[i-1])
                i -= 1
            else:
                result.append(str2[j-1])
                j -= 1
        
        # Add remaining chars
        while i > 0:
            result.append(str1[i-1])
            i -= 1
        while j > 0:
            result.append(str2[j-1])
            j -= 1
        
        # Reverse to correct order
        return "".join(result[::-1])
