class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        char = set(s)

        for i in range(len(s)):
            if s[i].swapcase() not in char:

                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])

                if len(left) >= len(right):
                    return left
                else:
                    return right

        return s                