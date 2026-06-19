class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        alt = 0
        for g in gain:
            alt += g
            res = max(res, alt)

        return res    
        