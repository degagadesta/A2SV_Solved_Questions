class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        min_heap = []
        heapq.heappush(min_heap, (nums1[0] + nums2[0], 0,0))

        ans = []
        visited = set((0,0))
        while k and min_heap:
            _, i,j = heapq.heappop(min_heap)

            if i + 1 < len(nums1) and (i+1, j) not in visited:
                heapq.heappush(min_heap, (nums1[i+1] + nums2[j], i+1, j))
                visited.add((i+1,j))
            if j + 1 < len(nums2) and (i, j+1) not in visited:
                visited.add((i, j+1))
                heapq.heappush(min_heap, (nums1[i] + nums2[j+1], i , j+1))
            ans.append([nums1[i], nums2[j]]) 
            k -= 1
        return ans            


        