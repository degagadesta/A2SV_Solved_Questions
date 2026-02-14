class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        temp = [[0] * len(mat) for i in range(len(mat))]
        for _ in range(4):
            temp = [[0] * len(mat) for i in range(len(mat))]
            for row in range(len(mat)):
                for col in range(len(mat)):
                    temp[row][col] = mat[col][row]

                temp[row].reverse()
                # if temp[row] != target[row] :
                #     return False
            if temp == target :
                return True 
            mat = temp       
        return False        

        
