class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Time Complexity : O( N * M * 4^N)
        """
        ROWS = len(board)
        COLS = len(board[0])
        WORD_LEN = len(word)
        visited = set()

        def dfs(r, c, i):
            if i == WORD_LEN:
                return True

            if r >= ROWS or r<0 or c<0 or c>=COLS or word[i] != board[r][c] or (r,c) in visited:
                return False

            visited.add((r,c))

            result =  dfs(r+1, c, i+1) or \
                dfs(r-1, c, i+1) or \
                dfs(r, c+1, i+1) or \
                dfs(r, c-1, i+1)
            
            visited.remove((r, c)) #backtracking

            return result

            
        
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i,j,0):
                    return True
        return False

