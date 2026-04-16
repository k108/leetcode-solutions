class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self.approach_2(s, t)

    def approach_2(self, s: str, t: str) -> int:
        '''
        Time Complexity : O(len(s) * len(t))
        Space Complexity : O(len(s) * len(t))
        '''
        '''
        Approach : Iterative DP

        Base Case :
        There is exactly 1 way to form an empty string,
        from any prefix of s -> by deleting everything

        f(i, 0) = 1
        '''
        T = len(t)
        S = len(s)

        # S * T
        dp = [[0]*(T+1) for _ in range(S+1)]

        # There is exactly 1 way to form an empty string,
        # from any prefix of s -> by deleting everything
        for i in range(S+1):
            dp[i][0] = 1
        
        for i in range(1, S+1):
            for j in range(1, T+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[S][T]

    def approach_1(self, s: str, t: str) -> int:
        '''
        Time Complexity : O(len(s) * len(t))
        Space Complexity : O(len(s) * len(t))
        '''
        '''
        Approach : DFS + Memoization

        How many ways can we match t[0..j] using s[0..i]?

        Every character in s gives us a binary choice:
        - use it
        - skip it
        '''
        
        @cache
        def dfs(i, j):
            # we reached end of both input string & target
            # so this subsequence of s equals t 
            if i == 0 and j == 0:
                return 1

            # we reached end of input string
            # but not target string
            # so this subsequence of s != t 
            if i == 0:
                return 0

            # we reached end of target string
            # but not input string
            # so this subsequence of s == t
            if j == 0:
                return 1

            # if characters match
            if s[i - 1] == t[j - 1]:
                # include this idx or exclude this idx
                return dfs(i-1, j-1) + dfs(i-1, j)
            
            # exclude this idx
            return dfs(i-1, j)
        
        return dfs(len(s), len(t))
