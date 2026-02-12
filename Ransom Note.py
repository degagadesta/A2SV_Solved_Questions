class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        cnt_ransom = Counter(ransomNote)
        cnt_magazine = Counter(magazine)

        for cnt in cnt_ransom :
            if cnt not in cnt_magazine or cnt_ransom[cnt] > cnt_magazine[cnt] :
                return False
        return True        
        
