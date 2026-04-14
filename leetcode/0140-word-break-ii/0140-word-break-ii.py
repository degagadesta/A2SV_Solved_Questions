class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        valid = set(wordDict)
        ans = []
        def helper(idx , wrd, words):
            if idx == len(s):
                t = "".join(wrd)
                if not t :
                    ans.append(" ".join(words))
                return      
            wrd.append(s[idx])
            t_w = "".join(wrd)
            if t_w in valid:
                words.append(t_w)
                helper(idx+1, [], words)
                words.pop()
            helper(idx+1 , wrd , words)
            wrd.pop()
        helper(0 , [], [])
        return ans                
        