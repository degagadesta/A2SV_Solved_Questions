class Solution:
    def minOperations(self, nums: List[int]) -> int:
        que = deque()
        cnt = 0
        for i in range(0,len(nums) -2) :
            if nums[i] == 0 :
                cnt += 1
                nums[i  + 1] = (nums[i+1] + 1) % 2
                nums[i + 2] = (nums[i+2] + 1) % 2
        if nums[-1] and nums[-2] :
            return cnt
        else:
            return -1            
