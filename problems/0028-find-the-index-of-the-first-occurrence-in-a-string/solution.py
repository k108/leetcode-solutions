class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        Time complexity: O(n * m)
        Space complexity: O(1)
        '''
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
