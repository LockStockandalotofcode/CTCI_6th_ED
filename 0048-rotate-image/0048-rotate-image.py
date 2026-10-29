import math
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # TAKE TRANSPOSE ACROSS MAIN DIAGONAL
        # IMAGE ACROSS Y-AXIS, OR REVERSING EACH ROW
        if not matrix:
            return
        
        n = len(matrix)
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            
        for r in range(n):
            for c in range(math.floor(n / 2)):
                matrix[r][c], matrix[r][n - 1 - c] = matrix[r][n - 1 - c], matrix[r][c]

        return