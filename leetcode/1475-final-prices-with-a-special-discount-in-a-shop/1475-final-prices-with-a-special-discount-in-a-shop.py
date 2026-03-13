class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        st = []
        for i in range(len(prices)-1, -1, -1) :
            while st and st[-1] > prices[i] :
                st.pop()
            t = prices[i]    
            if st :
                prices[i] -= st[-1]
            st.append(t)
        return prices            
        