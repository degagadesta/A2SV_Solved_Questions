class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        sorted_nums= sorted(cnt.items(),key=lambda item: item[1],reverse=True)
        nums_dict=dict(sorted_nums)
        index=0
        res=[]
        for i in nums_dict :
            if index<k:
                res.append(i)
                index+=1 
            else :
                break    
        return res    

        
