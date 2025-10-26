class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)

        if n == 0:
            return 0

        sign = +1
        i = 0
        base = 0
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        while i < n and s[i] == ' ': i += 1

        if i < n and (s[i] == '-' or s[i] == '+'):
            sign = 1 - 2 * (s[i] == '-')
            i += 1


        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            # before multiplying by 10 and adding another digit, 
            # we must check for overflow
            # if equal then multiplying by 10 is safe, but only if 
            # the next digit is ≤ the last digit of INT_MAX, which is 7
            if base > INT_MAX // 10 or (base == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN

            base = base * 10 + digit
            i += 1

        return base * sign
