class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mn = deque()
        mx = deque()
        left = 0 
        ans = 0
        for i in range(len(nums)):
            while mx and mx[-1] < nums[i] :
                mx.pop()
            mx.append(nums[i])
            while mn and mn[-1] > nums[i] :
                mn.pop()
            mn.append(nums[i])     
            while mn and mx and mx[0] - mn[0] > limit :
                if nums[left] == mn[0] :
                    mn.popleft()
                elif nums[left] == mx[0]:
                    mx.popleft()
                left += 1
            ans = max(ans, i - left + 1)
        return ans                     

        return ans        

        