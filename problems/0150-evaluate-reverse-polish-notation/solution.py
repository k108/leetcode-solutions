
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Time Complexity : O(n)
        Space Complexity : O(n), as we are using extra stack
        """
        # Reverse Polish / Postfix Notation : <Left Operand> - <Right Operand> - <Operator>
        # if token is not a operator push to stack
        # if token is a operator pop 2 elements form the stack,
        # perform the operation and push the result to the stack
        stack = []
        for token in tokens:
            if token == '+':
                operand_1 = stack.pop()
                operand_2 = stack.pop()
                stack.append(operand_2 + operand_1)
            elif token == '-':
                operand_1 = stack.pop()
                operand_2 = stack.pop()
                # order is important operand_2 - operand_1 and not operand_1 - operand_2
                stack.append(operand_2 - operand_1)
            elif token == '*':
                operand_1 = stack.pop()
                operand_2 = stack.pop()
                stack.append(operand_2 * operand_1)
            elif token == '/':
                operand_1 = stack.pop()
                operand_2 = stack.pop()
                # order is important operand_2 / operand_1 and not operand_1 / operand_2
                # round to zero
                stack.append(int(operand_2 / operand_1))
            else:
                stack.append(int(token))
            # print(operand_2, token, operand_1, "=", stack[-1])
            
        return stack[0]

        
