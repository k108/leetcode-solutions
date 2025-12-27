class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        def check_palindrome(left, right):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False
            return True
        
        while left < right:
            if s[left] != s[right]:
                return check_palindrome(left, right-1) or check_palindrome(left+1, right)
            left += 1
            right -= 1

        return True
