class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        total = 0
        total += nums[0]
        temp = set()
        temp.add(nums[0])
        for i in range(1, len(nums)) :
            total += nums[i]
        
            if((nums[i] + nums[i-1])%k == 0) :
                return True

            elif((total % k in temp and (total-nums[i] )%k != total % k) or (total % k) == 0) :
                return True
            
            temp.add(total % k )
        
        return False
