class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        left=0
        right=(num_rows*num_cols)-1

        while left<=right:
            mid=(left+right)//2
            # row_no = index_in_flattened_array // num_cols
            # col_no = index_in_flattened_array % num_cols
            # coordinate = (row_no, col_no)
            row = mid // num_cols
            col = mid % num_cols
            guess = matrix[row][col]

            if guess == target:
                return True
            elif guess < target:
                left=mid+1
            else:
                right=mid-1
        
        return False

        
