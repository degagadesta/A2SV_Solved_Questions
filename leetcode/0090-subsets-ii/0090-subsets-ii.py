class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        def helper(ind, comb):
            if ind >= len(nums):
                ans.add(tuple(comb))
                return
            comb.append(nums[ind])
            helper(ind+1, comb)
            comb.pop()
            helper(ind+1,comb)
        helper(0, [])
        ans = list(ans)
        temp = []
        for i in ans:
            temp.append(i)
        return temp    

        