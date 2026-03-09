class Solution:
    def minOperations(self, logs: List[str]) -> int:
        ans = 0
        cnt = 0
        for i in logs :
            i = i[:-1]
            if i == ".." :
                cnt = max(0, cnt - 1)
            elif i =="." :
                continue 
            else:
                cnt += 1
        return cnt               
        