from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        Time Complexity : O(r*c), we visit each cells exactly once.
        Space Complexity : O(r*c), this is required for storing visited.
        '''

        # check if source and target are 1
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1

        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        queue = deque()
        # starting point
        queue.append((0,0))
        visited.add((0,0))

        # offsets required for all 8 directions
        offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        # start with one 0 cell
        length = 1

        while queue:
            # loop through all the cells at the same distance
            for i in range(len(queue)):
                r, c = queue.popleft()

                if r == ROWS-1 and c == COLS-1:
                    return length

                for r_offset, c_offset in offsets:
                    new_row = r + r_offset
                    new_col = c + c_offset
                    
                    if 0 <= new_row < ROWS and 0 <= new_col < COLS and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited:
                        queue.append((new_row, new_col))
                        visited.add((new_row, new_col))
                    else:
                        continue
            
            # update the level or distance from source
            length+=1

        return -1


        
