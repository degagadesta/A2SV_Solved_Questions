class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        ans = [[0] * row for i in range(col)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans[j][i] = matrix[i][j]
                
        return ans        
        
