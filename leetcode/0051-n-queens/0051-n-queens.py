class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        cols = set()
        pd = set()
        nd = set()
        temp = [["."] * n for i in range(n)]
        def helper(row):
            if row == n:
                res = ["".join(i) for i in temp]
                ans.append(res)
                return 
            for col in range(n):
                if col in cols or row - col in pd or row + col in nd :
                    continue
                cols.add(col)
                pd.add(row - col)
                nd.add(row + col)
                temp[row][col] = "Q"
                helper(row+1)
                cols.remove(col)
                pd.remove(row - col)
                nd.remove(row + col)
                temp[row][col] = "."
        helper(0)
        return ans        


              


        