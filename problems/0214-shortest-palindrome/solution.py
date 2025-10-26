class Solution:
    def shortestPalindrome(self, s: str) -> str:
        '''
        Time Complexity : O(n)
        Space Complexity : O(n)
        '''
        '''
        We can think of it as,
        Find the longest palindrome substring starts from index 0
        We can easily build a palindrome string by inserting the reverse part of substring
        after such substring before the original string
        Input : abacd
        aba
        Output : dcabacd

        Find the longest palindrome substring starts from 0 :
        
        Build a temp string like this:
        s + "#" + reverse(s)
        Then we run KMP on it, the value in last cell will be our solution. 
        We use the lookup table in KMP to find the palindrome.
        
        We add "#" here to force the match in reverse(s) starts from its first index
        What we do in KMP here is trying to find a match between prefix in s and a postfix in reverse(s).
        The match part will be palindrome substring.
        Input : catacb
        Temp String: catacb # bcatac
        KMP table:
        c a t a c b # b c a t a c
        0 0 0 0 1 0 0 0 1 2 3 4 5
        In the last cell, we got a value 5. 
        It means in s we have a substring of length 5 that is palindrome.
        '''

        temp_s = s + '#' + s[::-1]
        n = len(temp_s)
        lps = [0]*n
        j = 0
        for i in range(1, n):
            while j > 0 and temp_s[i] != temp_s[j]:
                j = lps[j - 1]
            if temp_s[i] == temp_s[j]:
                j = j + 1

            lps[i] = j

        return s[lps[-1]:][::-1] + s      
