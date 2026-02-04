class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result=[]
        comment=0
        res=[]
        for src in source:
            i=0
            while i < (len(src)):
                if comment ==0 and i!= len(src)-1 and src[i]=='/' and src[i+1]=='/':
                    break
                if comment ==0 and i!= len(src)-1 and src[i]=='/' and src[i+1]=='*':
                    comment=1
                    i+=2
                    continue
                if i!= len(src)-1 and (comment ==1 and src[i]=='*' and src[i+1]=='/' ):
                    comment=0
                    i+=1
                elif comment == 0:
                    res.append(src[i])
                i+=1   
            if len(res)!=0 and comment ==0:
                temp="".join(res)  
                result.append(temp)
                res =[]

        return result                    


        
