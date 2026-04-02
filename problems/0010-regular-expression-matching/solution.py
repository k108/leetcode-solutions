class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.approach_5(s, p)

    def approach_5(self, s: str, p: str) -> bool:
        '''
        Time Complexity : O(len(s) * len(p))
        Space Complexity : O(len(s) * len(p))
        '''
        '''
        Approach : Suffix / Forward Iterative DP
        '''

        dp = [[False] * (len(p) + 1) for _ in range(len(s)+1)]
        dp[-1][-1] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                first_match = (
                    i < len(s) and 
                    p[j] in {s[i], '.'}
                )

                if j + 1 < len(p) and p[j+1] == '*':
                    dp[i][j] = (
                        dp[i][j+2] or
                        (first_match and dp[i+1][j])
                    )
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]

        return dp[0][0]

    def approach_4(self, s: str, p: str) -> bool:
        '''
        Time Complexity : O(len(s) * len(p))
        Space Complexity : O(len(s) * len(p))
        '''
        '''
        Approach : DP + Memoization

        Recurrence Relation :

        State :
        f(i, j) = does text[i:] match pattern[j:] ?
        suffix-based

        Base Case :
        f(i, j) = True    if j == m AND i == n
        f(i, j) = False   if j == m AND i < n

        i.e. If pattern is exhausted, string must also be exhausted

        Recurrence :

        f(i, j) =   {
                        if j == m:
                            return (i == n)

                        first_match = (i < n) AND (text[i] == pattern[j] OR pattern[j] == '.')

                        if j+1 < m AND pattern[j+1] == '*':
                            return f(i, j+2) OR (first_match AND f(i+1, j))

                        else:
                            return first_match AND f(i+1, j+1)
                    }

        f(0, 0) -> Answer
        '''
        @cache
        def dfs(i, j):
            if j == len(p):
                return i == len(s)

            first_match = (
                i < len(s) and 
                p[j] in {s[i], '.'}
            )

            if j + 1 < len(p) and p[j+1] == '*':
                return (
                    dfs(i, j+2) or
                    (first_match and dfs(i+1, j))
                )
            else:
                return first_match and dfs(i+1, j+1)

        return dfs(0, 0)

    def approach_3(self, s: str, p: str) -> bool:
        '''
        Time Complexity : O(len(s) * len(p))
        Space Complexity : O(len(p))
        '''
        '''
        Approach : 1D - DP

        prev[j] = dp[i-1][j]
        curr[j] = dp[i][j]

        Fix i ( let i be a constant ), vary j,

        Substitute into recurrence,

        Normal case :
        dp(i, j) = dp(i-1, j-1)
        Becomes:
        curr(j) = prev(j-1)

        * case :
        dp(i, j) = dp(i, j-2) OR dp(i-1, j)
        Becomes:
        curr(j) = curr(j-2) OR prev(j)

        dp(i-1, j) -> prev(j)
        dp(i-1, j-1) -> prev(j-1)
        dp(i, j-2) -> curr(j-2)
        
        '''
        n, m = len(s), len(p)

        prev = [False] * (m + 1)

        # Base case
        prev[0] = True

        # Initialize first row (empty string vs pattern)
        for j in range(2, m + 1):
            if p[j - 1] == '*':
                prev[j] = prev[j - 2]

        # Fill the DP table
        for i in range(1, n + 1):
            # reset
            curr = [False] * (m + 1)
            curr[0] = False

            for j in range(1, m + 1):

                # Case 1: normal char or '.'
                if p[j - 1] != '*':
                    curr[j] = (
                        prev[j - 1] and
                        (s[i - 1] == p[j - 1] or p[j - 1] == '.')
                    )

                # Case 2: '*'
                else:
                    curr[j] = (
                        curr[j - 2] or
                        (
                            (s[i - 1] == p[j - 2] or p[j - 2] == '.') and
                            prev[j]
                        )
                    )

            prev = curr

        return prev[m]

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
        prefix-based

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
