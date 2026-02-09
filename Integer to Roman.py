class Solution:
    def intToRoman(self, num: int) -> str:
       dictt ={
        1000 : "M",
        900:"CM",
        500: "D",
        400:"CD",
        100:"C",
        90:"XC",
        50:"L",
        40:"XL",
        10:"X",
        9:"IX",
        5:"V",
        4:"IV",
        1:"I"
       }
       num=str(num)
       index=0
       length=len(num)
       res=[]
       while index <length:
        temp = (int(num[index])) * (10** (length-index -1))
        if temp in dictt:
            res.append(dictt[temp])
            index+=1
            continue
        elif temp > 5 * (10**(length-index -1)):
            if (5*(10**((length-index -1)))) != 5000:
                res.append(dictt[(5*(10**((length-index -1))))])
                temp-=(5* (10**(length-index -1)))
        cnt = temp//10**(length-index -1)
        for l in range(cnt):
            res.append(dictt[10**(length-index -1)])
        index+=1
       return "".join(res) 

           
        
