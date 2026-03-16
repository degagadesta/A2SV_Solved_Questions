class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        cnt = 0
        t = nums[-1]

        for i in range(len(nums) - 2 , -1, -1) :
            if nums[i] > t :
                div = int(math.ceil(nums[i] / t))
                t = nums[i] // div
                cnt += div - 1
            else:
                t = nums[i]
        return cnt            

        return cnt        
        