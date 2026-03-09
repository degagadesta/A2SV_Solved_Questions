class Solution:
    def removeStars(self, s: str) -> str:
        sta = []
        for i in s :
            if i == "*" :
                if sta :
                    sta.pop()
            else :
                sta.append(i)
        return "".join(sta)        

        