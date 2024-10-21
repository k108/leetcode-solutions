
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Reverse Polish / Postfix Notation : <Left Operand> - <Right Operand> - <Operator>
        stack = []
        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                operand_1 = stack.pop()
                operand_2 = stack.pop()
                if token == '+':
                    stack.append(operand_2 + operand_1)
                elif token == '-':
                    stack.append(operand_2 - operand_1)
                elif token == '*':
                    stack.append(operand_2 * operand_1)
                elif token == '/':
                    stack.append(int(operand_2 / operand_1))
                # print(operand_2, token, operand_1, "=", stack[-1])
            
        return stack[0]

        
