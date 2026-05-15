class Solution:
    '''
    A very efficient trick comes from this key observation:

    Subtracting 1 from a number flips the rightmost 1 bit to 0 and turns all bits to its right into 1
    Performing n & (n - 1) removes the rightmost 1 bit from n
    '''
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res