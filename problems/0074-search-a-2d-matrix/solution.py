class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # T(n) = O(log(m*n))
        # S(n) = O(1)
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        def binary_search(matrix, low, high, key):
            if low > high:
                return False
            mid = (low+high) // 2
            # row_no = index_in_flattened_array // num_cols
            # col_no = index_in_flattened_array % num_cols
            # coordinate = (row_no, col_no)
            row = mid // num_cols
            col = mid % num_cols
            guess = matrix[row][col]
            if guess==key:
                return True
            elif guess<key:
                low = mid+1
                return binary_search(matrix, low, high, key)
            else:
                high = mid-1
                return binary_search(matrix, low, high, key)
        
        return binary_search(matrix, 0, (num_rows*num_cols)-1, target)

        
