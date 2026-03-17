class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def helper(x , n) :
            if n == 0 :
                return 1
            if n == 1 :
                return x
            temp = helper(x, n//2)
            if n % 2 :
                return (temp * temp * x) % (pow(10, 9) + 7)
            return (temp * temp) % (pow(10, 9) + 7)         

        ans = helper(5, int(math.ceil(n / 2)) )
        ans *= helper(4, n//2) 

        return ans  % (pow(10, 9) + 7)



        