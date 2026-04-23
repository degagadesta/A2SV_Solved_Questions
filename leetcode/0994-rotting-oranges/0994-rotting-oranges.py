class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [(-1,0), (1,0),(0,-1),(0,1)]
        m , n = len(grid) , len(grid[0])
        def isValid(r, c):
            return r >= 0 and c >= 0 and r < m and c < n and grid[r][c] != 0
        queue = deque()
        tt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append([i , j])
                    grid[i][ j] = -1
                elif grid[i][j] == 0 :
                    tt += 1 
        if tt == m * n:
            return 0               
        cnt = -1

        while queue:
            length = len(queue)
            for _ in range(length):
                i , j = queue.popleft()
                for r , c in directions:
                    if isValid(r + i , c + j) and grid[r + i][c + j] != -1:
                        queue.append([r + i, c + j])
                        grid[r + i][c + j] = -1
            cnt += 1  
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2 or grid[i][j] == 1:
                    return -1
        return cnt                       



        