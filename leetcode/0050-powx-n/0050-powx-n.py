class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper (x, n):
            if n == 0 :
                return 1
            if n == 1 :
                return x
            temp = helper( x, n//2)
            if n % 2:
                return temp *  temp * x 

            return temp * temp
        if n < 0 :
            return 1 / (helper(x, abs(n)))
        else:
            return helper(x,n)
               
                               
        