class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0 :
            return 1
        num = int(math.log(n, 2) + 1 )
        return 2 ** num - 1 - n

        