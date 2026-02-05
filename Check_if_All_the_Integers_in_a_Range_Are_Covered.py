class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ranges.sort()
        res = [ranges[0]]
        
        for i in range(1, len(ranges)):
            if res[-1][1] >= ranges[i][0]:
                res[-1][1] = max(res[-1][1], ranges[i][1])
            else:
                res.append(ranges[i])
        
        total = 0
        for i in res:
            for cnt in range(i[0], i[1]+1):
                if left <= cnt <= right:
                    total += cnt
        
        expected = (right * (right + 1)) // 2 - ((left - 1) * left) // 2
        
        return total == expected
