class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        cnt = 0
        sp = set()
        vis = set()
        for ch in word:
            if ch >= "a":
                if ch.upper() in sp and ch not in vis:
                    cnt += 1
                    vis.add(ch)
                    vis.add(ch.upper())
            else:
                if ch.lower() in sp and ch not in vis: 
                    cnt += 1
                    vis.add(ch)
                    vis.add(ch.lower())
            sp.add(ch)
        return cnt     





        