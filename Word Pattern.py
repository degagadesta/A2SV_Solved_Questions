class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(s) != len(pattern):
            return False

        temp = defaultdict(list)
        for index in range(len(s)) :
            if pattern[index] in temp :
                temp[pattern[index]].append(index)
            else:
                temp[pattern[index]].append(index)   

        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] == s[j] and pattern[i] != pattern[j] :
                    return False

        for patt in temp :
            t = temp[patt[0]]
            char = s[t[0]]
            for index in t:
                if s[index] != char :
                    return False
                    
        return True            



        
