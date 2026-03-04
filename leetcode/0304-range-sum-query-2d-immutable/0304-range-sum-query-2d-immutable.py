class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.pref = []
        temp = [0] * (len(matrix[0])  + 1 )
        self.pref.append(temp)
        for i in range(len(matrix)) :
            temp = [0]
            for j in range(len(matrix[0])) :
                total = 0
                total += self.pref[i ][j+1] + temp[j] + matrix[i][j] - self.pref[i][j]
                temp.append(total)
            self.pref.append(temp)
   

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pref[row2 + 1][col2 + 1] - self.pref[row1][col2 + 1] - self.pref[row2 + 1][col1] + self.pref[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)