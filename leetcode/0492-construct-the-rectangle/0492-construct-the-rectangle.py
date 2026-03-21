class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        temp = int(pow(area, 0.5))
        while temp < area :
            if area % temp == 0 :
                t = max([temp , area // temp])
                return [max([temp , area // temp]),min([temp , area // temp])]
            else :
                temp += 1
        return [area , 1]            
        