class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows=len(grid)
        cols=len(grid[0])
        visited = set()
        max_area = 0

        def bfs(r, c):
            area = 0
            queue = []
            visited.add((r, c))
            queue.append((r, c))
            while queue:
                row, col = queue.pop(0)
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (0<=r<rows) and (0<=c<cols) and grid[r][c]==1 and (r,c) not in visited:
                        area+=1
                        queue.append((r, c))
                        visited.add((r, c))
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visited:
                    area = 1
                    area += bfs(r, c)
                    max_area = max(max_area, area)

        return max_area

        
