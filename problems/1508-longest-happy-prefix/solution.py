class Solution:
    def longestPrefix(self, s: str) -> str:
        '''
        Use KMP Longest Prefix Suffix Table
        At the last index (i = n - 1),
        lps[-1] gives the length of the longest proper prefix 
        of the entire string that is also a suffix

        lps table tells us, for each prefix, how much of it overlaps with its suffix
        lps[-1] gives the overlap length for the entire string
        Taking s[:lps[-1]] extracts that overlapping part, the longest prefix also serving as suffix
        '''
        n = len(s)
        lps = [0]*n
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]
            if s[i] == s[j]:
                j = j + 1

            lps[i] = j
        
        return s[:lps[-1]]    
