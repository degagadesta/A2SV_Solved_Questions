class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = Counter(answers)
        ans = 0
        for i in cnt :
           if cnt[i] <= i+1 :
            ans += i + 1
           else:
            temp = cnt[i]
            while temp > i+1  :
                temp -= (i+1)
                ans += i+1
            ans += i + 1
        return ans       