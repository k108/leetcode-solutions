class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self.approach_1(s, t)
    
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
