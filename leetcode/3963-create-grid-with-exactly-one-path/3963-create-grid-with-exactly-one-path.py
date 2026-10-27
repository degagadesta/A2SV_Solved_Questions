class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        res = [[] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == n-1:
                    res[i].append(".")
                else:
                    res[i].append("#")
        for  i in range(m):
            res[i] = "".join(res[i])
        return res                   