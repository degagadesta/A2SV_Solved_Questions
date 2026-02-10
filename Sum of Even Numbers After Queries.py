class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans=[]
        cnt=0
        for i in nums:
            if i%2==0:
                cnt+=i
        for i in queries:
            if nums[i[1]]%2==0:
                nums[i[1]]+=i[0]
                if nums[i[1]]%2==0:
                    cnt+=i[0]
                else:
                    cnt-=(nums[i[1]]-i[0])
            else:
                nums[i[1]]+=i[0]
                if nums[i[1]]%2==0:
                    cnt+=nums[i[1]]
            ans.append(cnt)
        return ans            


        
