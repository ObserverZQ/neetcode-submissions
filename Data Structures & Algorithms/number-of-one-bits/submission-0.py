class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            res += n & 1 # use & with 1 to get the rightmost bit
            n >>= 1 # shift 1 bit rightwards
        return res