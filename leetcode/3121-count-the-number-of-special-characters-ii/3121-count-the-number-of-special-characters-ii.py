class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        cn = Counter(word)
        cnt = 0
        sp = set()
        vis = set()
        inv = set()
        for ch in word:
            if ch >= "a":
                sp.add(ch)
                cn[ch] -= 1
            else:
                if ch not in inv:
                    if cn[ch.lower()] > 0:
                        inv.add(ch)
                        continue
                if ch.lower() in sp and ch not in vis and ch not in inv: 
                    print(ch)
                    cnt += 1
                    vis.add(ch)
                    vis.add(ch.lower())
        return cnt
        