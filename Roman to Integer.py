class Solution:
    def romanToInt(self, s: str) -> int:
        temp ={
            "M":1000,
            "CM": 900,
            "D":500,
            "CD":400,
            "C":100,
            "XC":90,
            "L":50,
            "XL":40,
            "X":10,
            "IX":9,
            "V":5,
            "IV":4,
            "I":1
        }
        i = 0
        num=0
        while i < len(s):
            if i != len(s)-1 and temp[s[i]] < temp[s[i+1]]:
                num+= (temp[(s[i]+s[i+1])])
                i+=2
            else:
                num+=temp[s[i]]
                i+=1   
        return num        


        
