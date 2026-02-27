class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        cnt = Counter(s)

        temp = defaultdict(list)
        t = set()
        for i in range(len(s)):
            if s[i] not in t :
                temp[s[i]] = ([i, s.rindex(s[i])])
                t.add(s[i])
        t2 = []
        for i in temp :
            t2.append(temp[i]) 

        temp = []
        temp.append(t2[0])
        for i in range(1, len(t2)) :
            if temp[-1][1] >= t2[i][0] :
                temp[-1][1] = max(temp[-1][1] , t2[i][1])
            else:
                temp.append(t2[i])
        ans = []
        for i in range(len(temp)):
            ans.append(temp[i][1] - temp[i][0] + 1)

        return ans                






        
        
