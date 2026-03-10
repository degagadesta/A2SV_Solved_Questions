class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums2)
        st = []
        for i in range(len(nums2) - 1, -1, -1) :
            if st :
                while st and st[-1] < nums2[i] :
                    st.pop()
                if st :
                    ans[i] = st[-1]
                
            st.append(nums2[i])  
        temp = defaultdict(int)      
        for i in range(len(nums2)) :
            temp[nums2[i]] = ans[i]
        ans = []    
        for i in  nums1 :
            ans.append(temp[i])
        return ans    
