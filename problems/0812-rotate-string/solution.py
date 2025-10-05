class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        '''
        We can easily see whether it is rotated if B can be found in (A + A).
        '''
        return len(s) == len(goal) and goal in s+s
