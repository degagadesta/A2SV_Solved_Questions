class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        temp = Counter(nums)
        mx_num = 0
        mx_cnt = 0
        for i in temp :
            if temp[i] > mx_cnt:
                mx_cnt = temp[i]
                mx_num = i  
        cnt = 0          

        for i in range(len(nums)):
            if nums[i] == mx_num:
                cnt += 1

            if cnt >  (i+1)/2  and mx_cnt - cnt > ((len(nums)-i -1 ) /2):
                return i
        return -1        
        
