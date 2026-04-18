class Solution:
    def mirrorDistance(self, n: int) -> int:
        a = list(str(n))
        a.reverse()
        a = "".join(a)
        a = int(a)
        return abs(n - a)
        