class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        left = 0
        ans =[]
        for i in range(len(nums)) :
            while queue and queue[-1] < nums[i] :
                queue.pop()
            queue.append(nums[i])
            if i >= k -1 :
                ans.append(queue[0]) 
                if nums[left] == queue[0]:
                    queue.popleft()
                left += 1    
        return ans                
        