class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        return self.approach_3(s1, s2, s3)

    def approach_3(self, s1: str, s2: str, s3: str) -> bool:
        '''
        Time Complexity : O(len(s1) * len(s2))
        Space Complexity : O(min(len(s1), len(s2)))
        '''
        '''
        Approach : Bottom-Up DP - 1D DP

        We only require the information from the cells dp[i - 1][j] and 
        dp[i][j - 1], i.e. the cell above the current row and the cell 
        to the left of the current column.

        Collapse 2D to 1D

        dp[j] = dp[i][j]

        dp[j] (before update) -> dp[i-1][j] (UP)
        dp[j-1] (already updated) -> dp[i][j-1] (LEFT)

        dp[j] -> old value -> dp[i-1][j]
        dp[j-1] -> new value -> dp[i][j-1]

        State :
        dp[j] = whether s1[:i] and s2[:j] can form s3[:i+j]

        Recurrence :

        For each i >= 1, j >= 1:

        dp[j] =
            (dp[j]     AND s1[i-1] == s3[i+j-1])   <- from UP (old dp[j])
        OR (dp[j-1]   AND s2[j-1] == s3[i+j-1])   <- from LEFT (new dp[j-1])

        '''
        if len(s1) + len(s2) != len(s3):
            return False

        if len(s2) > len(s1):
            s1, s2 = s2, s1

        dp = [False] * (len(s2) + 1)

        dp[0] = True
        
        # First row
        for j in range(1, len(s2) + 1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]

        for i in range(1, len(s1)+1):
            # First column (for each i)
            dp[0] = dp[0] and s1[i-1] == s3[i-1]

            for j in range(1, len(s2)+1):
                ans1 = False
                ans2 = False

                if s3[i+j-1] == s1[i-1]:
                    ans1 = dp[j]

                if s3[i+j-1] == s2[j-1]:
                    ans2 = dp[j-1]

                dp[j] = ans1 or ans2

        return dp[len(s2)]

    def approach_2(self, s1: str, s2: str, s3: str) -> bool:
        '''
        Time Complexity : O(len(s1) * len(s2))
        Space Complexity : O(len(s1) * len(s2))
        '''
        '''
        Approach : Bottom-Up 2D DP
        '''
        if len(s1) + len(s2) != len(s3):
            return False

        dp = [[False]*(len(s2)+1) for _ in range(len(s1)+1)]

        dp[0][0] = True

        # Can the first i characters of s1 
        # alone form the first i characters of s3?
        # First i-1 chars of s1 already matched s3
        # The next character must also match
        # Previous prefix is valid AND current character matches
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

        # Can the first j characters of s2 
        # alone form the first j characters of s3?
        # First j-1 chars of s2 already matched s3
        # The next character must also match
        # Previous prefix is valid AND current character matches
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):

                ans1 = False
                ans2 = False

                if s3[i+j-1] == s1[i-1]:
                    ans1 = dp[i-1][j]

                if s3[i+j-1] == s2[j-1]:
                    ans2 = dp[i][j-1]

                dp[i][j] = ans1 or ans2

        return dp[len(s1)][len(s2)]

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
