class Solution:
    def isPalindrome(self, s: str) -> bool:
        N = len(s) 
        s = s.lower()
        i = 0
        j = N-1
        while i<j:
            while i<N and s[i] not in 'abcdefghijklmnopqrstuvwxyz1234567890' :
                i+=1
            while j>-1 and s[j] not in 'abcdefghijklmnopqrstuvwxyz1234567890':
                j-=1
            if i<j and s[i]!=s[j]:
                return False
            else:
                i+=1
                j-=1
        return True

        
