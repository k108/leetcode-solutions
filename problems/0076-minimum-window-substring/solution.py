class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Time Complexity : O(n + m) -> O(n)
        Space Complexity : O(k) or O(1) constant under fixed charset
        '''

        if not s or not t or len(s) < len(t):
            return ""

        # create freq array of target string
        char_freq = defaultdict(int)
        for ch in t:
            char_freq[ch] += 1

        min_window = (0, float('inf'))
        count = len(t)
        start_idx = 0

        # expand window
        for end_idx, ch in enumerate(s):
            # expand the right pointer until all the characters of t are covered
            if char_freq[ch] > 0:
                count -= 1
            char_freq[ch] -=1
            
            # contract window
            if count == 0:
                # once all the characters are covered, 
                # move the left pointer and ensure that all the characters 
                # are still covered to minimize the subarray size
                while True:
                    start_char = s[start_idx]
                    if char_freq[start_char] == 0:
                        # encountered mandatory character
                        break
                    char_freq[start_char] += 1
                    start_idx += 1
                
                # update min window
                if end_idx - start_idx < min_window[1] - min_window[0]:
                    min_window = (start_idx, end_idx)
                
                # adjust the character count for the character being removed from the window
                char_freq[s[start_idx]] += 1
                # character is no longer in the window
                count += 1
                # move to right
                start_idx += 1

        return "" if min_window[1] > len(s) else s[min_window[0]:min_window[1]+1]
