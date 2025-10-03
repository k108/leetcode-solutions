class Solution:
    def largestOddNumber(self, num: str) -> str:
        '''
        If last digit of a number is odd then number is odd, 
        and if last digit of a number is even then number is even
        '''
        for i in range(len(num)-1, -1, -1):
            if num[i] in {'1', '3', '5', '7', '9'}:
                return num[:i+1]
        return ''
