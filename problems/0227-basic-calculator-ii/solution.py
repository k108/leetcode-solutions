class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        result = 0
        pre_op = '+'
        s += '+'
        stack = []
        for c in s:
            # read number digit by digit and form number
            if c in '0123456789':
                num = num*10 + int(c)
            elif c in '-+*/':
                if pre_op == '+':
                    stack.append(num)
                elif pre_op == '-':
                    stack.append(-num)
                elif pre_op == '*':
                    stack[-1]=stack[-1] * num
                elif pre_op == '/':
                    stack[-1]=int(stack[-1] / num)
                num = 0
                pre_op = c
        
        return sum(stack)

        
