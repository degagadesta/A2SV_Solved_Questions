class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        vis = set()
        def bfs(node,vis):
            queue = deque([node])
            while queue:
                i = queue.popleft()
                for j in range(len(isConnected)):
                    if j not in vis:
                        if isConnected[i][j]:
                            queue.append(j)
                            vis.add(j)
        ans = 0
        for i in range(len(isConnected)):
            if i not in vis:
                vis.add(i)
                ans += 1
                bfs(i,vis)     
        return ans                     
        