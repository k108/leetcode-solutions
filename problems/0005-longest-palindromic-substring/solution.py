class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Time Complexity : O(n^2)
        """
        N = len(s)
        result = ""
        result_len = 0
        for i in range(N):
            # odd length
            left = i
            right = i
            while left>=0 and right<N and s[left] == s[right]:
                if result_len < right - left + 1:
                    result = s[left:right+1]
                    result_len = right - left + 1
                left-=1
                right+=1

            # even length
            left = i
            right = i+1
            while left>=0 and right<N and s[left] == s[right]:
                if result_len < right - left + 1:
                    result = s[left:right+1]
                    result_len = right - left + 1
                left-=1
                right+=1

        return result
            

        
