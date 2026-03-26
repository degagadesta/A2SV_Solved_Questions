class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(comb):
            if len(comb) == len(nums):
                ans.append(comb.copy())
                return 
            for i in range(len(nums)):
                if nums[i] in temp:
                    continue
                comb.append(nums[i])
                temp.add(nums[i])
                backtrack(comb)    
                comb.pop()
                temp.remove(nums[i])
        ans = []
        temp = set()
        backtrack([])
        return ans        

                
        