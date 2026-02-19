class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        res = 1
        temp = points[0]
        for i in range(1,len(points)):
            if temp[1] >= points[i][0]:
                temp[0] = max(temp[0], points[i][0])
                temp[1] = min(temp[1], points[i][1])
            else:
                res += 1
                temp = points[i]    
        return res        

        





        
