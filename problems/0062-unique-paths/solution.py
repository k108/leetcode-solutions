class Solution:
    def uniquePaths(self, R: int, C: int) -> int:
        '''
        Time Complexity : O(R * C)
        Space Complexity : O(C)
        '''
        '''
        Bottom-Up \ Iterative DP :-
        We just need to know the previous rows results
        We just need to know the previous column results
        Last row and last colum will contain all 1's and
        outside them out of bounds can be thought of 0's
        '''
        prev_row = [0] * C

        for r in range(R -1, -1, -1):
            curr_row = [0] * C
            curr_row[C - 1] = 1
            for c in range(C-2, -1, -1):
                curr_row[c] = curr_row[c + 1] + prev_row[c]
            prev_row = curr_row
        
        return prev_row[0]
