class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        length= len(strs[0])
        for i in range(length):
            ch=strs[0][i]
            for j in range(len(strs)):
                if i >= len(strs[j]) or strs[j][i]!= ch :
                    return res
            else:
                res+= ch        
        
