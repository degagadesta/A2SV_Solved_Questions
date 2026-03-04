class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro = 1 
        ans = []
        for i in range(len(nums)) :
            ans.append(pro)
            pro *= nums[i]

        pro = 1
        for i in range(len(nums) - 1, - 1, -1) :
            ans[i] *= pro
            pro *= nums[i]

        return ans        
        