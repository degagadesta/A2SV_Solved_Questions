class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        columns = set() 

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == 0:
                    rows.add(row)
                    columns.add(col)

        for row in rows :
            for column in range(len(matrix[0])):
                matrix[row][column] = 0

        for column in columns :
            for row in range(len(matrix)):
                matrix[row][column] = 0


        
