class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:        
            ans=[]
            if len(changed)%2 != 0:
                return []
            temp = Counter(changed)
            temp =dict(sorted(temp.items()))

            for i in temp:
                while temp[i]>0 :
                    if i==0 :
                         if temp[0] % 2==0:
                            i = temp[0] // 2
                            temp[0] = 0
                            for i in range(i):
                                ans.append(0)
                         else:
                            return []  
                         break                  
                    if (i*2 in temp)and temp[i*2] > 0 :
                        ans.append(i)
                        temp[i] -= 1
                        temp[i*2] -= 1
                    else:    
                        return []   
            return ans         

        
