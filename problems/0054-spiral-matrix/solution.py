class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Time Complexity: O(m*n)
        Space Complexity: O(1)
        """
        # we keep 4 pointers left, right, top and bottom 
        # at each corner of the matrix and we traverse
        # left -> right, then increase top
        # top -> bottom, then decrease right
        # right -> left, then decrease bottom
        # bottom -> top, then increase left
        # while left < right and top < bottom
        ROWS=len(matrix)
        COLUMNS=len(matrix[0])
        left=0
        right=COLUMNS
        top=0
        bottom=ROWS
        result = []

        while left < right and top < bottom:
            # get every i in top row
            for i in range(left, right):
                result.append(matrix[top][i])
            top+=1
            
            # get every i in right col
            for i in range(top, bottom):
                result.append(matrix[i][right-1])
            right-=1
            
            # for single row or single column matrix
            if not (left < right and top < bottom):
                break

            # get every i in bottom row
            for i in range(right-1, left-1, -1):
                result.append(matrix[bottom-1][i])
            bottom-=1

            # get every i in left col
            for i in range(bottom-1, top-1, -1):
                result.append(matrix[i][left])
            left+=1

        return result



        
