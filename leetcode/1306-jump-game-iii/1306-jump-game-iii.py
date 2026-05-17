class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque()
        queue.append(start)
        vis = set()
        vis.add(start)
        while queue:
            node = queue.popleft()
            if not arr[node]:
                return True
            if node + arr[node] not in vis and  node + arr[node] < len(arr):
                queue.append(node + arr[node])
                vis.add(node + arr[node])
            if node - arr[node] not in vis and node - arr[node] >= 0:
                queue.append(node - arr[node])
                vis.add(node - arr[node])        
        return False        
        