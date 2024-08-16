class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {'(' : ')', '{' : '}', '[' : ']'}
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                if stack:
                    top_element = stack.pop()
                    if mapping[top_element] == c:
                        continue
                    else:
                        return False
                else:
                    return False

        return True if not stack else False

        
