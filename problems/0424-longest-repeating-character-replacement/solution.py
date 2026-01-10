class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Time Complexity : O(n)
        Space Complexity : O(1)
        '''
        '''
        longest substring where (length - max occurrence) <= k
        '''
        L = len(s)
        freq = [0]*26
        start = 0
        max_freq = 0
        max_len = 0
        for end in range(L):
            idx = ord(s[end]) - ord('A')
            freq[idx] += 1
            max_freq = max(max_freq, freq[idx])
            while end - start + 1 - max_freq > k:
                freq[ord(s[start]) - ord('A')] -= 1
                start += 1
            max_len = max(max_len, end - start + 1)
        return max_len
