class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap = []
        for stone in stones:
            heapq.heappush(min_heap,-1 * stone)

        while len(min_heap) > 1:
            y  = heapq.heappop(min_heap)
            x  = heapq.heappop(min_heap)
            y *= -1
            x *= -1 
            if y != x :
                heapq.heappush(min_heap, -1 *(y - x))
        return -1 * min_heap[0] if min_heap else 0       
        