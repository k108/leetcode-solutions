class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.approach_1(s, p)

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
