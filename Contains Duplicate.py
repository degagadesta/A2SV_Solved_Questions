class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        temp=Counter(nums)
        nums =dict(sorted(temp.items(),key = lambda item: item[1], reverse=True))

        for num in nums:
            return nums[num] >= 2    


        
