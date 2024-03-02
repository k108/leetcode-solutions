class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    row_fingerprint = f'ROW-{r}-{board[r][c]}'
                    column_fingerprint = f'COLUMN-{c}-{board[r][c]}'
                    box_fingerprint = f'BOX-{r//3}-{c//3}-{board[r][c]}'

                    if row_fingerprint in seen or column_fingerprint in seen or box_fingerprint in seen:
                        return False

                    seen.add(row_fingerprint)
                    seen.add(column_fingerprint)
                    seen.add(box_fingerprint)

        return True


        
