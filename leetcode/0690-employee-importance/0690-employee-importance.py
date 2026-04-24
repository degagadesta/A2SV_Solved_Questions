"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        imp = defaultdict(int)
        for emp in employees:
            imp[emp.id] = emp.importance
            for i in emp.subordinates:
                graph[emp.id].append(i)
        queue = deque()
        visited = set()
        queue.append(id)
        ans = 0
        ans += imp[id]
        visited.add(id) 
        while queue:
            node = queue.popleft()
            for i in graph[node]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
                    ans += imp[i]
        return ans                   
        