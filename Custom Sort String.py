class Solution:
    def customSortString(self, order: str, s: str) -> str:
        cnt = Counter(s)
        temp = []
        for i in range(len(order)):
            while cnt[order[i]] > 0 :
                temp.append(order[i])
                cnt[order[i]] -= 1
        for i in cnt :
            while cnt[i] > 0 :
                temp.append(i)
                cnt[i] -= 1    
        return "".join(temp)            
        
