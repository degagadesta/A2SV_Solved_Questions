class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        minn = minutes / 5
        res = abs(minn - (hour+ (minutes / 60)))
        return min((res/12) * 360 , 360 -((res/12) * 360))
        