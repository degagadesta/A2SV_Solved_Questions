class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = [[] for i in range(n)]
        indegree = [0] * n
        for u , v in edges:
            graph[v].append(u)

        ans = [[] for i in range(n)]    

        def dfs(ver, visited):
            visited.add(ver)
            for par in graph[ver]:
                if par not in visited:
                    dfs(par, visited)
            return visited
        for  i in range(n):
            res = (dfs(i,set()))
            res.remove(i)
            res = list(res)
            res.sort()
            ans[i]= res.copy()
        return ans               

            # if not graph[ver]:
            #     ans[ver].extend(st)
            #     return
            # st.append(ver)    
            # for adj in graph[ver]:
            #     dfs(adj , st)
            # st.pop()
            # ans[ver].extend(st)
        # for i in range(n):
        #     if not indegree[i]:
        #         dfs(i , [])
        # for i in range(n):
        #     temp = list(set(ans[i]))
        #     temp.sort()
        #     ans[i] = temp
        # return ans    
                    

