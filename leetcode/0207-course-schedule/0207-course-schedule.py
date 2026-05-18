class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ind = [0] * numCourses
        graph = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            graph[v].append(u)
            ind[u] += 1
        order = []
        queue = deque()
        for i in range(numCourses):
            if not ind[i]:
                queue.append(i)
        while queue:
            node = queue.popleft()
            order.append(node)
            for adj in graph[node]:
                ind[adj] -= 1
                if not ind[adj]:
                    queue.append(adj)


        return len(order) == numCourses                         
        