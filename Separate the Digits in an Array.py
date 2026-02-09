class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        t=[]
        for i in nums:
            t.append(str(i))
        temp="".join(t)
        ans=[]
        for i in temp:
            ans.append(int(i))
        return ans    
        
