class Solution:
    def isPalindrome(self, x: int) -> bool:
        res=""
        temp= str(x)
        l= len(temp)-1
        while l>=0:
            res+=temp[l]
            l-=1
        return res==temp    
