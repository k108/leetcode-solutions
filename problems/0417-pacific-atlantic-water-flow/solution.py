class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(row, col, visited, previous_height):
            if (
                ((row, col) in visited) or \
                row < 0 or row == ROWS or \
                col < 0 or col == COLS or \
                heights[row][col] < previous_height \
            ):
                return None
            
            # collecting valid cells
            visited.add((row, col))

            dfs(row+1, col, visited, heights[row][col])
            dfs(row-1, col, visited, heights[row][col])
            dfs(row, col+1, visited, heights[row][col])
            dfs(row, col-1, visited, heights[row][col])

        # we do the inverse, we start from boundaries and climb up
        for col in range(COLS):
            # start from boundary of pacific ocean - first row
            dfs(0, col, pacific, heights[0][col])
            # start from boundary of atlantic ocean - last row
            dfs(ROWS-1, col, atlantic, heights[ROWS-1][col])

        for row in range(ROWS):
            # start from boundary of pacific ocean - first column
            dfs(row, 0, pacific, heights[row][0])
            # start from boundary of atlantic ocean - last column
            dfs(row, COLS-1, atlantic, heights[row][COLS-1])

        result = []
        for row in range(ROWS):
            for col in range(COLS):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])
        return result

        
