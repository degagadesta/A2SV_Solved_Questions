class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res=Counter(nums)
        temp=set()
        for i in res:
            if res[i] > len(nums)//3:
                temp.add(i)
        return list(temp)      
        
        
