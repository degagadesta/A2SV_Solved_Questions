class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse = True)
        ans = 0 
        for i in citations :
            if i > ans :
                ans += 1
        return ans        


        
