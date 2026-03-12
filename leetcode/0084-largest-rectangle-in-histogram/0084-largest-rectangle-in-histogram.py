class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left = [-1] * len(heights)
        st = []
        for i in range(len(heights)) :
            while st and st[-1][0] >= heights[i] :
                st.pop()
            if st :
                left[i] = st[-1][1]    
            st.append([heights[i], i])
        right = [len(heights)] * len(heights)
        st = []
        for i in range(len(heights) - 1, -1, -1 ):
            while st and st[-1][0] >= heights[i] :
                st.pop()
            if st :
                right[i] = st[-1][1]    
            st.append([heights[i], i])
        ans = 0    
        for i in range(len(right)) :
            right[i] = right[i] - left[i] - 1
            ans = max(ans, right[i] * heights[i])
        return ans        



