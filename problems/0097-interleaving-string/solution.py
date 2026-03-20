class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.approach_1(s1, s2, s3)

    def approach_1(self, s1: str, s2: str, s3: str) -> bool:
        '''
        Time Complexity : O(len(s1) * len(s2))
        Space Complexity : O(len(s1) * len(s2))
        '''

        '''
        Approach : DFS with Memoization

        Recurrence Relation :

        State :
        dp[i][j] = Can first i characters of s1 and the first j characters of s2,
        form the first i+j characters of s3

        Base Case :
        dp[0][0] = True, as both empty strings can form an empty string

        Recurrence :
        dp[i][j] = dp[i-1][j], if s3[i+j-1] == s1[i-1]
        dp[i][j] = dp[i][j-1], if s3[i+j-1] == s2[j-1]

        Answer : dp[len(s1)][len(s2)]
        '''

        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def dfs(i, j):

            if i == 0 and j==0:
                return True

            ans1 = False
            ans2 = False

            if i > 0 and s3[i+j-1] == s1[i-1]:
                ans1 = dfs(i-1, j)
                if ans1:
                    return ans1
            if j > 0 and s3[i+j-1] == s2[j-1]:
                ans2 = dfs(i, j-1)

            return ans1 or ans2

        return dfs(len(s1), len(s2))  
