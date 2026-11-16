class Solution:
    def digitSum(self, s: str, k: int) -> str:
        temp = list(s)
        while len(temp) > k:
            temp2 = []
            i = 0
            summ = 0
            for num in temp:
                if i == k:
                    i = 1
                    temp2.extend(str(summ))
                    summ = int(num)
                else:
                    i += 1
                    summ += int(num)
            temp2.extend(str(summ))  
            temp = temp2.copy()
        return "".join(temp)    



        