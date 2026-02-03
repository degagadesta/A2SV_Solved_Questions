class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        x=n
        while True:
            if x%n==0 and x%2==0:
                return x
            x+=1    

        
