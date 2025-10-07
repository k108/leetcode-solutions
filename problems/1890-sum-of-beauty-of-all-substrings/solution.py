class Solution:
    def beautySum(self, s: str) -> int:
        '''
        Time Complexity : O(26 * n^2)
        Space Complexity : O(1)
        '''

        '''
        - Iterate through all possible substrings of the input string.
        - For each substring, maintain a frequency count of characters.
        - Calculate the beauty for each substring by finding the difference 
        between the maximum and minimum frequency (excluding zero frequencies).
        - Sum up the beauties of all substrings and return the result.
        '''

        ans = 0
        for i in range(len(s)):
            freq = [0]*26
            max_f = 0
            for j in range(i, len(s)):
                e = ord(s[j]) - ord('a')
                freq[e] += 1

                # the max for each iteration is either the current max 
                # or the freq we just updated
                if freq[e] > max_f:
                    max_f = freq[e]

                min_f = float("+inf")

                for k in range(26):
                    if freq[k] > 0 and freq[k] < min_f:
                        min_f = freq[k]

                ans += max_f - min_f

        return ans
