class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []
        def backtrack(idx , temp):
            if idx == n:
                
                for i in range(len(temp)-1):
                    if temp[i] == temp[i+1]:
                        return
                res.append("".join((temp.copy())))
                return 
            temp.append("a")
            backtrack(idx+1, temp)
            temp.pop()
            temp.append("b")
            backtrack(idx+1, temp)
            temp.pop()
            temp.append("c")
            backtrack(idx+1, temp)
            temp.pop()  
        backtrack(0, [])
        res.sort()
        if k > len(res):
            return "" 
        return res[k-1]                 

