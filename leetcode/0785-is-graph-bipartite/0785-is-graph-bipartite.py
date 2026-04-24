class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = set()
        temp = [2] * len(graph)
        queue = deque()
        def bfs(ver):
            visited.add(ver)
            temp[ver] = 0
            queue.append(ver)
            col = 0
            while queue:
                l = len(queue)
                for _ in range(l):
                    n = queue.popleft()
                    for node in graph[n]:
                        if temp[node] == col:
                                return False
                        if node not in visited:
                            queue.append(node) 
                            visited.add(node) 
                            temp[node] = (col + 1) % 2
                col = (col + 1) % 2
            return True                         
        for i in range(len(graph)):
            if i not in visited:
                if not bfs(i):
                    return False
        return True            
                        


        