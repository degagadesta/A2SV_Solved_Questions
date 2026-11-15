class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        even = 0
        odd = 0
        ans = 0
        summ = 0
        for num in arr:
            summ += num
            if summ % 2:
                ans += 1
                ans += even
                odd += 1
            else:
                even += 1
                ans += odd
        return ans % (10 ** 9 + 7)      
        