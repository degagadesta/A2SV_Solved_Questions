class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(ver , visited):
            if ver == destination:
                return True
            visited.add(ver)
            for neigh in node[ver]:
                if neigh not in visited:
                    if dfs(neigh , visited):
                        return True
            return False           

        node = [[] for i in range(n) ]
        for i in edges:
            node[i[0]].append(i[1])
            node[i[1]].append(i[0])

        return dfs(source , set())            