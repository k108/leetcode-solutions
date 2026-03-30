class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.approach_2(s, p)

    def approach_2(self, s: str, p: str) -> bool:
        '''
        Time Complexity : O(len(s) * len(p))
        Space Complexity : O(len(s) * len(p))
        '''
        '''
        Approach : Iterative DP
        '''
        n, m = len(s), len(p)

        # dp[i][j] = does s[0:i] match p[0:j]
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        # Base case
        dp[0][0] = True

        # Initialize first row (empty string vs pattern)
        for j in range(2, m + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):

                # Case 1: normal char or '.'
                if p[j - 1] != '*':
                    dp[i][j] = (
                        dp[i - 1][j - 1] and
                        (s[i - 1] == p[j - 1] or p[j - 1] == '.')
                    )

                # Case 2: '*'
                else:
                    dp[i][j] = (
                        dp[i][j - 2] or
                        (
                            (s[i - 1] == p[j - 2] or p[j - 2] == '.') and
                            dp[i - 1][j]
                        )
                    )

        return dp[n][m]

    def approach_1(self, s: str, p: str) -> bool:
        '''
        Time Complexity : O(len(s) * len(p))
        Space Complexity : O(len(s) * len(p))
        '''
        '''
        '.' Matches any single character.​​​
        '*' Matches zero or more of the preceding element

        When we see *:

        Do we skip it OR use it?

        Skip -> (i, j-2)
        Use  -> (i-1, j)

        We stay at j (because * can repeat)
        We reduce i

        while (matches x):
            consume
        OR
        skip entirely

        LOOP OR SKIP

        Cases :
        1. s[i] == p[j] or p[j] == '.' , current characters must match, then previous prefixes must match
        2. p[j] == '*'
         - p[j-1] == '.', matches any character
         - p[j-1] != '.', matches only prev character

        State :
        dp[i][j] = does s[0:i] match p[0:j] i.e. prefix match

        Base Case :
        dp[0][0] = True
        Empty string matches empty pattern

        When i = 0: 
        Pattern must look like: a*b*c*... 
        i.e. Can an empty string match pattern p[0:j]
        Only when the pattern can represent nothing.

        Which naturally works via: dp[0][j] = dp[0][j-2]

        '''
        @cache
        def dfs(i, j):
            # Base case
            if j == 0:
                return i == 0

            # Case 2: '*'
            if p[j-1] == '*':
                return (
                    # Skip x* (0 occurrences)
                    # Ignore both x and *
                    # If pattern ends with x*, we can ignore it
                    dfs(i, j-2) or
                    (
                        # Use x* (1+ occurrences)
                        # We consume one character from s if it matches x
                        i > 0 and
                        # first match
                        (s[i-1] == p[j-2] or p[j-2] == '.') and
                        dfs(i-1, j)
                    )
                )

            # Case 1: normal char or '.'
            return (
                i > 0 and
                # first match
                (s[i-1] == p[j-1] or p[j-1] == '.') and
                dfs(i-1, j-1)
            )

        return dfs(len(s), len(p))
