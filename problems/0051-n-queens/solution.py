class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        pos_diag = set() # (r + c)
        neg_diag = set() # (r - c)

        board = [["."]*n for i in range(n)]
        result = []

        def dfs(row):
            # base case
            if row >= n:
                result.append([ "".join(r) for r in board])
                return
            
            for col in range(n):
                if ( col in cols ) or ( row+col in pos_diag ) or ( row-col in neg_diag ) :
                    continue
                else:

                    cols.add(col)
                    pos_diag.add(row+col)
                    neg_diag.add(row-col)
                    board[row][col] = "Q"

                    dfs(row+1)

                    # backtracking
                    cols.remove(col)
                    pos_diag.remove(row+col)
                    neg_diag.remove(row-col)
                    board[row][col] = "."

        dfs(0)

        return result                 
        
