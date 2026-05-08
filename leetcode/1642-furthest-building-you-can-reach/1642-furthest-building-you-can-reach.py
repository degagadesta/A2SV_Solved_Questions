class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        arr = []
        for i in range(1, len(heights)):
            if heights[i] <= heights[i-1]:
                continue
            heapq.heappush(arr,  (heights[i] - heights[i-1]))
            if len(arr) > ladders:
                if arr[0] > bricks:
                    return i-1
                bricks -= arr[0]
                heapq.heappop(arr)    
        return len(heights) -1           
        