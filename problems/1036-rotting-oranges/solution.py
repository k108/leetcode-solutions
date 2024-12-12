from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Time Complexity = O(n*m)
        Space Complexity = O(n*m), for queue
        '''

        # We use multi-source BFS here
        ROWS=len(grid)
        COLS=len(grid[0])
        minutes = 0
        queue = deque()
        fresh_oranges_count = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==1:
                    fresh_oranges_count+=1
                elif grid[r][c]==2:
                    queue.append((r,c))

        while queue and fresh_oranges_count>0:
            # pop all the rotting oranges in the queue
            # although we are appending rotting oranges to the queue
            # range(len(queue)) is executed once and not at every iteration of the for loop
            # so we are doing multi-source BFS here
            # we are traversing each level from multiple start nodes
            for i in range(len(queue)):
                r, c = queue.popleft()

                neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbors:
                    # if in bounds and fresh, make rotten
                    if (min(r + dr, c + dc) >= 0 and
                        r + dr < ROWS and c + dc < COLS and
                        grid[r + dr][c + dc] == 1):
                        grid[r + dr][c + dc] = 2
                        fresh_oranges_count-=1
                        queue.append((r + dr, c + dc))

            minutes += 1

        if fresh_oranges_count>0:
            return -1

        return minutes


        
