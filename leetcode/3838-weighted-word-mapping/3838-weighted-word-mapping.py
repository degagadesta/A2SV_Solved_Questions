class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = []
        for word in words:
            temp = 0
            for ch in word:
                temp += weights[ord(ch) - 97]
            temp = 25 - (temp%26)
            ans.append(chr(temp + 97))
        res = "".join(ans)
        return res     
        