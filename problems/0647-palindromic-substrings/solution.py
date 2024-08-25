class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Time Complexity : O(n^2)
        """
        N = len(s)
        count = 0
        for i in range(N):
            # odd length
            left = i
            right = i
            while left>=0 and right<N and s[left] == s[right]:
                count+=1
                left-=1
                right+=1

            # even length
            left = i
            right = i+1
            while left>=0 and right<N and s[left] == s[right]:
                count+=1
                left-=1
                right+=1

        return count
            

        
        
