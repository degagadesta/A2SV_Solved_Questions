class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        left = 0
        cnt1 = 0 
        temp = defaultdict(int)
        dis = set()
        for right in range(len(nums)) :
            temp[nums[right]] += 1
            dis.add(nums[right])
            while len(dis) > k :
                temp[nums[left]] -= 1
                if temp[nums[left]] == 0 :
                    dis.remove(nums[left])
                left += 1
            cnt1 +=  right - left + 1

        cnt2 = 0
        left = 0
        k -= 1
        temp = defaultdict(int)
        dis = set()   
        for right in range(len(nums)) :
            temp[nums[right]] += 1
            dis.add(nums[right])
            while len(dis) > k :
                temp[nums[left]] -= 1
                if temp[nums[left]] == 0 :
                    dis.remove(nums[left])
                left += 1
            cnt2 += right - left + 1
        return cnt1 - cnt2    


        
