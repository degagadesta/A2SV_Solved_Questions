class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        ans = 0
        i = 1

        while i < (len(piles)- len(piles)//3):
            ans  += piles[i]
            i += 2
        return ans    


        
