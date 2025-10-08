class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        moves = 0
        stack = []
        for c in s:
            if c == "(":
                stack.append("(")
            elif not stack:
                moves += 1
            elif c == ")" and stack[-1] == "(":
                stack.pop()
        return moves + len(stack)
