class Solution:
    def maxDepth(self, s: str) -> int:
        count_p, max_d = 0, 0

        for c in s:
            if c == '(':
                count_p += 1
                # the max for each iteration is either the current max 
                # or the count we just updated
                if max_d < count_p:
                    max_d = count_p
            elif c == ')':
                count_p -= 1
        
        return max_d       
