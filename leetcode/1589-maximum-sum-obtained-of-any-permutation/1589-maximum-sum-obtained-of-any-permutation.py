class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pref = [0] * len(nums)
        for req in requests :
            pref[req[0]] += 1
            if req[1] < len(nums) - 1 :
                pref[req[1] + 1] -= 1
        for i in range(1, len(pref)) :
            pref[i] += pref[i - 1]    
        nums.sort(reverse = True)
        ans = 0
        index = 0
        pref.sort(reverse = True)
        for p in pref :
            if p <= 0 :
                break
            ans += (p * nums[index] )
            index += 1   
        return ans % (pow(10, 9) + 7 )     



        
        