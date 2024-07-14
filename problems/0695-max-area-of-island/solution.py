class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        visited = set()
        max_area = 0

        def dfs(r, c):
            if (0 > r) or (r == rows) or (0 > c) or (c == cols) or (grid[r][c] == 0) or ((r, c) in visited):
                return 0

            visited.add((r, c))
            return (1 + dfs(r+1, c) + \
                        dfs(r-1, c) + \
                        dfs(r, c+1) + \
                        dfs(r, c-1)
                    )

        for r in range(rows):
            for c in range(cols):
                max_area = max(max_area, dfs(r,c))

        return max_area
