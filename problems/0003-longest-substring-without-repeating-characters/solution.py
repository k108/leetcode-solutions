class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_len = 1
        occurence = {}
        start, end = 0, 0
        while(end < len(s)):
            if s[end] in occurence:
                old_start = start
                start = occurence[s[end]]
                start += 1
                for k in range(old_start, start):
                    del occurence[s[k]]
            occurence[s[end]]=end
            max_len = max(max_len, (end-start)+1)
            end += 1
        return max_len


