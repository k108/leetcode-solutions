class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows=len(grid)
        cols=len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c):
            queue = []
            visited.add((r, c))
            queue.append((r, c))
            while queue:
                row, col = queue.pop(0)
                directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row+dr, col+dc
                    if (0<=r<rows) and (0<=c<cols) and grid[r][c]=="1" and (r,c) not in visited:
                        queue.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visited:
                    bfs(r, c)
                    islands+=1

        return islands

