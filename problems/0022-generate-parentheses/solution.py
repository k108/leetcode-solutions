class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        combination = []
        def dfs(open_p, close_p):
            # base case
            # valid if count of open parantheses == count of closed parantheses == n
            if open_p == n and open_p == close_p:
                result.append("".join(combination))
                return

            # only add open paranthesis if count of open parantheses < n
            if open_p < n:
                combination.append("(")
                dfs(open_p+1, close_p)
                # combination is global variable, so we need to clean-up
                combination.pop()

            # only add closed paranthesis if count of closed < count of open parantheses 
            if close_p < open_p:
                combination.append(")")
                dfs(open_p, close_p+1)
                # combination is global variable, so we need to clean-up
                combination.pop()

        dfs(0, 0)
        return result

        
