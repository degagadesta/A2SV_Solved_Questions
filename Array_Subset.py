#User function Template for python3
from collections import Counter
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        res=True
        c=Counter(a)
        # Your code here
        for i in b:
            if i not in c or c[i]==0:
                res=False
                break
            else:
                c[i]-=1
        return res        
    
    
    
    
