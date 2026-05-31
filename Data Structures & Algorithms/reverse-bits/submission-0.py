class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        i = 0
        while i < 32:
            res <<= 1
            if n > 0:
                res += n & 1
                n >>= 1
            i += 1
        return res