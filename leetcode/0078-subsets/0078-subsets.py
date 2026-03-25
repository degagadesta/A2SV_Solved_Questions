class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        temp = set()
        def helper(ind , comb) :
            if ind == len(nums) :
                ans.append(comb.copy())
                return  
            comb.append(nums[ind])
            helper(ind + 1, comb)
            comb.pop()
            helper(ind+1, comb)

        ans = []
        helper(0, [])
        return ans    
        