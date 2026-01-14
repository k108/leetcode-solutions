class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        return self.approach_1(s, k)

    def approach_2(self, s: str, k: int) -> int:
        pass
    
    def approach_1(self, s: str, k: int) -> int:
        '''
        Time Complexity : O(n)
        Space Complexity : O(1)
        '''
        '''
        Assume there is no constraints like the k,
        Given a string convert it to a string with all same characters with minimal changes =
        (length - max occurrence)
        Apply the at most k changes constraint and maintain a sliding window,
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
