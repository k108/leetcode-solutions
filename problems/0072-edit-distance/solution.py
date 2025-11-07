class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        Time Complexity : O(s_len * t_len)
        Space Complexity : O(s_len * t_len)
        '''

        '''
        If we reach the end of one word then, 
        the minimum number of transformations is simply to 
        insert the rest of the other word

        We either match the currently indexed characters in both strings, or mismatch. 
        In the first case, we don't incur any penalty, and we can continue to compare
        the rest of the strings by recursing on the rest of both strings.
        In the case of a mismatch, we either insert, delete, or replace.
        '''

        # Top-Down + Memoization
        # dp(r, c) = edit distance between word1[:r] and word2[:c]
        @lru_cache(None)
        def dp(r,c):
            if r == 0: return c # c inserts
            if c == 0: return r # r inserts
            if word1[r-1] == word2[c-1]:
                return dp(r-1, c-1)
            return min(dp(r, c-1), dp(r-1, c), dp(r-1,c-1)) + 1

        return dp(len(word1), len(word2))
