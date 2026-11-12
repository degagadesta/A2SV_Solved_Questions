class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = 1
        mx_inc = 1
        mx_dec = 1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                mx_dec += 1
                mx_inc = 1
            elif nums[i] < nums[i+1]:
                mx_inc += 1
                mx_dec = 1
            else:
                mx_dec = 1
                mx_inc = 1
            ans = max(ans, mx_dec,mx_inc)    
        return max(ans, mx_inc,mx_dec)                
        