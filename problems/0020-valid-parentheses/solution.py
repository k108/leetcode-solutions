class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paranthesis_mapping = {'(':')', '{':'}', '[':']'}
        for symbol in s:
            if symbol in ['(', '{', '[']:
                stack.append(symbol)
            else:
                if stack == []:
                    return False
                else:
                    top_symbol = stack.pop()
                    if paranthesis_mapping[top_symbol] != symbol:
                        return False
        if stack == []:
            return True
        else:
            return False
        
