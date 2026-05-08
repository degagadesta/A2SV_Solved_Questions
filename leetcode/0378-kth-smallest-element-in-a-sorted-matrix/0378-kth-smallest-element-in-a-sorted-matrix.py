class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m,n = len(matrix), len(matrix)
        min_heap = []
        cur = [0] 
        for i in range(min(k,n)):
            heapq.heappush(min_heap, (matrix[i][0],i,0))
        ans = float("-inf")
        for i in range(k):
            ans , r , c = heapq.heappop(min_heap)
            if c + 1 < n :
                heapq.heappush(min_heap, (matrix[r][c+1], r, c+1))
        return ans        


