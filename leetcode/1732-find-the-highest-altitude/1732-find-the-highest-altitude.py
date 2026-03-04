class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        nums = [0]
        for i in gain :
            nums.append(i + nums[-1])
            
        return (max(nums))    
        