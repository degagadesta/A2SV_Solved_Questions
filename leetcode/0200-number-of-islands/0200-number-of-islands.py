class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        ans = 0
        def isValid(i,j):
            return i >= 0 and j >= 0 and i < len(grid) and j < len(grid[0])
        def dfs(i , j):
            grid[i][j] = "0"
            for di in directions:
                nr = i + di[0]
                nc = j + di[1]
                if isValid(nr, nc) and grid[nr][nc] == "1":
                    dfs(nr , nc)
                 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    ans += 1
        return ans            
