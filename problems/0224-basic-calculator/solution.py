class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        sign = 1
        result = 0
        stack = []
        for c in s:
            # read number digit by digit and form number
            if c in '0123456789':
                # for consecutive digits 98 => 9x10 + 8 = 98
                num = num*10 + int(c)
            elif c in '-+()':
                # Add num to result, because we need to empty num for next integer value.
                # Update sign based on c
                if c in '+-':
                    result += num*sign
                    sign = -1 if c == '-' else 1
                    num = 0
                # we need to calculate sum of integers within ()
                # [result, sign]
                # reset : result = 0, sign = 0
                elif c == '(':
                    stack.append(result)
                    stack.append(sign)
                    result = 0
                    sign = 1
                # Example : 2-(3+4), Here res=3, num=4, sign=1 stack [2, -]
                # res +=sign*num -> calculate sum for num first, then pop items from stack, res=7
                # res *=stack.pop() - > Pop sign(+ or -) to multiply with res, res = 7*(-1)
                # res +=stack.pop() - > Pop integer and add with prev. sum, res = -7 + 2 - 5
                elif c == ')':
                    result += num*sign
                    result *= stack.pop()
                    result += stack.pop()
                    num = 0
        
        return result + num*sign

        
