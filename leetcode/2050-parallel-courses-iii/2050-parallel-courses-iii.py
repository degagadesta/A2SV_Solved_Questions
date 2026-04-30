class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        indegree = [0] * n
        graph = [[] for i in range(n)]
        for u , v in relations:
            graph[u-1].append(v-1)
            indegree[v-1] += 1


        queue = deque()
        m_time = [0 for i in range(n)]
        for i in range(n):
            if not indegree[i]:
                queue.append(i)
                m_time[i] += time[i]
        while queue:
            node = queue.popleft()
            for adj in graph[node]:
                indegree[adj] -= 1
                m_time[adj] = max(m_time[adj], m_time[node] + time[adj])
                if not indegree[adj]:
                    queue.append(adj)

        return max(m_time)                    


        