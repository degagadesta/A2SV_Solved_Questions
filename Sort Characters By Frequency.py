class Solution:
    def frequencySort(self, s: str) -> str:
        temp = Counter(s)
        temp = dict(sorted(temp.items(),key = lambda item: item[1], reverse=True))
        ans = []
        for i in temp :
            while temp[i] > 0:
                ans.append(i) 
                temp[i] -= 1
        return "".join(ans)        
        
