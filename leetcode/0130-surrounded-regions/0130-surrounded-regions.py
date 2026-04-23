class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(-1,0), (1,0),(0,-1),(0,1)]
        m , n = len(board) , len(board[0])

        def isValid(r,c):
            return r >= 0 and c >= 0 and r < m and c < n
        def dfs(ver):
            if not isValid(ver[0], ver[1]) or board[ver[0]][ver[1]] != "O":
                return
            board[ver[0]][ver[1]] = "V"     
            for di in directions:
                dfs([ver[0] + di[0] , ver[1] + di[1]])

        for i in range(m):
            dfs([i, 0])
            dfs([i , n-1])
        for j in range(n):
            dfs([0,j])
            dfs([m-1, j])

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "V":
                    board[i][j] = "O"                     


            


        