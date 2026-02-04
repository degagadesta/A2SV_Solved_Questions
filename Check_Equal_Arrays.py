class Solution:
    def checkEqual(self, a, b) -> bool:
        a.sort()
        b.sort()
        if len(a) != len(b):
            return False
        res=True        
        for i in range(len(a)):
            if a[i]!=b[i]:
                res=False
                break
        return res            
        #code here
