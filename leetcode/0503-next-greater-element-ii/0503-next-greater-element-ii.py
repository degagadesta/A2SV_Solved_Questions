class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        temp = nums + nums[:len(nums)]
        st = []
        for i in range(len(temp)-1,-1,-1) :
            while st and st[-1] <= temp[i] :
                st.pop()
            if st and i < len(nums):
                ans[i] = st[-1]
            st.append(temp[i])   
        return ans    
        