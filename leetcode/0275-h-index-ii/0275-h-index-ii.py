class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = -1
        right = len(citations) 
        n  = len(citations)
        while left + 1 < right :
            mid = (right + left) // 2

            if mid >= n - citations[mid] :
                right = mid
            else:
                left = mid    
        return n - right        

        
                