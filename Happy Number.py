class Solution:
    def isHappy(self, n: int) -> bool:
        checked= set()
        while n not in checked:
            if n<10 and n!= 1 and n!= 7:
                return False
            temp=0 
            checked.add(n)   
            while n>0:
                y= n%10
                temp+= y**2
                n//=10
            n=temp
        return n==7 or n==1        

        
