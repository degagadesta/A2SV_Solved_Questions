class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        temp ={}
        for i in range(len(s)):
            temp[indices[i]]=s[i]   
        res=dict(sorted(temp.items()))
        ans=[]
        for i in res:
            ans.append(res[i])
        return "".join(ans)            
        
