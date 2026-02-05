class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans=0
        for word in words :
            temp=Counter(chars)
            cnt=0
            for ch in word:
                if ch in temp and temp[ch]!=0 :
                    temp[ch] -=1
                    cnt+=1
                else:
                    break
            if cnt == len(word):
                ans+=cnt
        return ans                    
        
