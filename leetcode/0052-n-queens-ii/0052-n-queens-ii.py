class Solution:
    def totalNQueens(self, n: int) -> int:
        ans = 0
        temp = [["."]*n for i in range(n)]
        nd = set()
        pd = set()
        cols = set()
        def backtrack(row):
            nonlocal ans
            if row == n:
                ans += 1
                return 
            for col in range(n):
                if col in cols or row - col in pd or row + col in nd :
                    continue
                cols.add(col)
                pd.add(row - col)
                nd.add(row + col)
                temp[row][col] = "Q"
                backtrack(row + 1)
                cols.remove(col)
                pd.remove(row - col)
                nd.remove(row + col)
                temp[row][col] = "."
        backtrack(0)
        return ans        

        