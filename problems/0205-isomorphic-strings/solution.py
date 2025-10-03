from collections import defaultdict

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        Whenever a character appears in s, 
        it must map to the same character in t as it did before
        so we track last seen idx
        0 → means not seen yet
        i + 1 → real index shifted by 1
        '''
        last_seen_s, last_seen_t = [0]*200, [0]*200
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if last_seen_s[ord(s[i])] != last_seen_t[ord(t[i])]:
                return False
            last_seen_s[ord(s[i])] = i + 1
            last_seen_t[ord(t[i])] = i + 1
        return True
