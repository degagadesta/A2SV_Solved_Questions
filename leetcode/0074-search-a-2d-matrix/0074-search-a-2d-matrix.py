class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = -1
        row = len(matrix)
        col = len(matrix[0])
        right = row * col 
        while left + 1 < right :
            mid = (left + right) // 2 
            r = mid // col
            c = (mid % col)
            if matrix[r][c] == target :
                return True
            elif matrix[r][c] > target :
                right = mid
            else:
                left = mid 
        return False               

        