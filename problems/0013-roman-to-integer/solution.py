class Solution:
    def romanToInt(self, s: str) -> int:
        '''
        In Roman Numerals :
        When a smaller value appears before a larger value, it represents subtraction, 
        When a smaller value appears after or equal to a larger value, it represents addition.
        '''
        roman_to_int = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
            # 'IV': 4,
            # 'IX': 9,
            # 'XL': 40,
            # 'XC': 90,
            # 'CD': 400,
            # 'CM': 900
        }
        
        ans = 0

        for i in range(len(s)):
            if i < len(s) - 1 and roman_to_int[s[i]] < roman_to_int[s[i+1]] :
                ans -=  roman_to_int[s[i]]
            else:
                ans +=  roman_to_int[s[i]]
        
        return ans
