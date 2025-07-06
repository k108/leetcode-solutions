from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        '''
        Time Complexity : O(n)
        Space Complexity : O(n)
        '''
        N = len(s)
        queue = deque([0])
        max_till_now = 0

        if s[N-1] != '0':
            return False
        
        # BFS
        while queue:
            i = queue.popleft()
            for j in range(max(i + minJump, max_till_now + 1), min(i + maxJump + 1, N)):
                if s[j] == '0':
                    if j == N - 1: 
                        return True
                    queue.append(j)
            
            max_till_now = maxJump + i

        return False
