class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        n = len(graph)
        def dfs(ver, temp):
            if ver == n - 1:
                ans.append(temp.copy())
                return
            for i in graph[ver]:
                temp.append(i)
                dfs(i, temp)
                temp.pop()
        temp = []        
        temp.append(0)
        dfs(0, temp)   
        return ans         
        