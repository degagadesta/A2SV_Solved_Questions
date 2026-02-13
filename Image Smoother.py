class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        R, C = len(img), len(img[0])
        ans = [[0] * C for _ in range(R)]

        for i in range(R):
            for j in range(C):
                temp = img[i][j]
                count = 1 

                if i - 1 >= 0 and j - 1 >= 0: 
                    temp += img[i-1][j-1]
                    count += 1
                if i - 1 >= 0:                
                    temp += img[i-1][j]
                    count += 1
                if i - 1 >= 0 and j + 1 < C:  
                    temp += img[i-1][j+1]
                    count += 1
                if j - 1 >= 0:                
                    temp += img[i][j-1]
                    count += 1
                if j + 1 < C:               
                    temp += img[i][j+1]
                    count += 1
                if i + 1 < R and j - 1 >= 0:  
                    temp += img[i+1][j-1]
                    count += 1
                if i + 1 < R:                
                    temp += img[i+1][j]
                    count += 1
                if i + 1 < R and j + 1 < C:  
                    temp += img[i+1][j+1]
                    count += 1

                ans[i][j] = temp // count
                
        return ans
