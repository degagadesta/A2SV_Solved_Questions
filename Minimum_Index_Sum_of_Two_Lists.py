class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        temp={}
        for i in range(len(list1)):
            temp[list1[i]]=i
        res=len(list1)+len(list2) 
        ans=[]   
        for i in range(len(list2)):
            if list2[i] in temp:
                res= min(res, temp[list2[i]]+i) 
                if res==temp[list2[i]]+i:
                    if len(ans)>0 and temp[ans[-1]] != res:
                        ans=[]
                    ans.append(list2[i])
                    temp[list2[i]]=res
        return ans             
