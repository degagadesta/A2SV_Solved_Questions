class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        temp = set()
        for i in nums:
            l = len(i) 
            s = 0
            for j in range(l) :
                if i[j] == "1" :
                    s += 2 ** (l - j - 1)
            temp.add(s)
        for i in range(2 ** len(nums[0]) + 1) :
                if i not in temp :
                    ans = i 
                    break
        temp = []
        while ans > 0 :
            temp.append(str(ans%2))
            ans //= 2
        cnt = len(nums[0]) - len(temp)
        while cnt > 0 :
            temp.append("0")
            cnt -= 1
        temp.reverse()    
        return "".join(temp)                          


        