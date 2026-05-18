class Solution:
    def minJumps(self, arr: List[int]) -> int:
        temp = defaultdict(list)
        for i in range(len(arr)):
            temp[arr[i]].append(i)
        res = 0
        queue = deque()
        queue.append(0)
        vis = set()
        vis.add(0)
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.popleft()
                if node == len(arr)-1:
                    return res
                if node + 1 not in vis and node+1 < len(arr):
                    queue.append(node+1)
                    vis.add(node+1)
                if node-1 not in vis and node-1 >= 0 :
                    queue.append(node-1)
                    vis.add(node-1)
                for ind in temp[arr[node]]:
                    if ind != node and ind not in vis:
                        queue.append(ind)
                        vis.add(ind)
                del temp[arr[node]]        
            res += 1            


        