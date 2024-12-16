class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        # inverse approach :-
        # leak and only start from the boundary
        # we traverse the boundary and if we find an "O"
        # we need to eliminate all the "O" that can be reached from here
        # i.e. we do DFS from borders

        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r,c):
            # mark as protected
            board[r][c]='#'
            if 0<=r+1<ROWS and 0<=c<COLS and (r+1,c) and board[r+1][c]=="O":
                dfs(r+1,c)
            if 0<=r-1<ROWS and 0<=c<COLS and (r-1,c) and board[r-1][c]=="O":
                dfs(r-1,c)
            if 0<=r<ROWS and 0<=c+1<COLS and (r,c+1) and board[r][c+1]=="O":
                dfs(r,c+1)
            if 0<=r<ROWS and 0<=c-1<COLS and (r,c-1) and board[r][c-1]=="O":
                dfs(r,c-1)

        # dfs from 'O's on border
        for r in range(ROWS):
            # left down
            if board[r][0]=="O": dfs(r,0)
            # right down
            if board[r][COLS-1]=="O": dfs(r,COLS-1)

        for c in range(COLS):
            # top left to right
            if board[0][c]=="O": dfs(0,c)
            # bottom left to right
            if board[ROWS-1][c]=="O": dfs(ROWS-1,c)

        # flip surrounding regions
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    # change to 'X'
                    board[r][c] = 'X'
                elif board[r][c] == '#':
                    # change back to 'O'
                    board[r][c] = 'O'

            


        
