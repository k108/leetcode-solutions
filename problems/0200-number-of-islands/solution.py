class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
            
        ROWS = len(grid)
        COLUMNS = len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):

            if 0<=r+1<ROWS and 0<=c<COLUMNS and (r+1,c) not in visited and grid[r+1][c]=="1":
                visited.add((r+1,c))
                dfs(r+1, c)
            if 0<=r-1<ROWS and 0<=c<COLUMNS and (r-1,c) not in visited and grid[r-1][c]=="1":
                visited.add((r-1,c))
                dfs(r-1, c)
            if 0<=r<ROWS and 0<=c+1<COLUMNS and(r,c+1) not in visited and grid[r][c+1]=="1":
                visited.add((r,c+1))
                dfs(r, c+1)
            if 0<=r<ROWS and 0<=c-1<COLUMNS and (r,c-1) not in visited and grid[r][c-1]=="1":
                visited.add((r,c-1))
                dfs(r, c-1)

        for r in range(ROWS):
            for c in range(COLUMNS):
                if grid[r][c]=="1" and (r,c) not in visited:
                    visited.add((r,c))
                    dfs(r, c)
                    islands+=1

        return islands
        
