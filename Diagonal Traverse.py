class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]: 
        temp = defaultdict(list)

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                temp [row + col].append(mat[row][col])
        ans = []

        for i in temp :
            if i % 2 != 0:
                for num in temp[i]:
                    ans.append(num)
            else:
                temp[i].reverse()
                for num in temp[i]:
                    ans.append(num)
        return ans            


