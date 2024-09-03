from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        time = 0
        fresh_count = 0

        dequeue = deque()
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    dequeue.append((r,c))
                if grid[r][c]==1:
                    fresh_count+=1

        while dequeue and fresh_count>0:
            time+=1
            # for each level
            for _ in range(len(dequeue)):
                i, j = dequeue.popleft()

                for r, c in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                    if (r>=0 and r<ROWS) and (c>=0 and c<COLS) and grid[r][c]==1:
                        grid[r][c]=2
                        fresh_count-=1
                        dequeue.append((r,c))

        if fresh_count > 0:
            return -1

        return time




        
