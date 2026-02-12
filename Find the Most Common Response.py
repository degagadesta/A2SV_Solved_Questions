class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        temp = {}
        for i in range(len(responses)):
            temp[i] = set(responses[i])
        res =[]
        for i in temp:
            for resp in temp[i]:
                res.append(resp)

        cnt = Counter(res)

        mx_cnt = 0 
        mx_key = ""

        for i in cnt:
            if cnt[i] > mx_cnt :
                mx_key = i
                mx_cnt = cnt[i]
            elif cnt[i]== mx_cnt :
                if i < mx_key:
                    mx_key=i
        return mx_key                



        
