class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def helper(ind, comb):
            if ind >= len(nums):
                for i in range(1, len(comb)):
                    if comb[i-1] > comb[i]:
                     return
                if len(comb) >= 2 :     
                    ans.add(tuple(comb.copy()))
                return 
            comb.append(nums[ind])
            helper(ind+1, comb)
            comb.pop()
            helper(ind+1, comb)

        helper(0, [])
        ans = list(ans)
        return ans        
        