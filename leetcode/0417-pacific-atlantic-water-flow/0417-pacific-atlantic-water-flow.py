class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights) , len(heights[0])
        pac , atl = set() , set()
        directions = [(-1,0) , (1,0) , (0,-1) , (0,1)]

        def isValid(r, c):
            return r >= 0 and c >= 0 and r < rows and c < cols
        def dfs(r , c, visit , mx):
            if not isValid(r,c) or heights[r][c] < mx  or (r,c) in visit:
                return
            visit.add((r,c))
            for i , j in directions:
                dfs(r + i , c + j , visit , heights[r][c])
        for r in range(rows):
            dfs(r,0,pac,heights[r][0])
            dfs(r,cols-1, atl, heights[r][cols-1])
        for c in range(cols):
            dfs(0,c,pac,heights[0][c])
            dfs(rows-1, c,atl, heights[rows-1][c])

        res = []
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pac and (i,j) in atl:
                    res.append([i, j])
        return res                                    

        