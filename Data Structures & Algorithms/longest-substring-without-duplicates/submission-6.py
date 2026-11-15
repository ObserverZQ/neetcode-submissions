class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        contained = set()
        res = 0
        cur = 0
        while r < len(s):
            while s[r] in contained:
                contained.remove(s[l])
                cur -= 1
                l += 1
            contained.add(s[r])
            cur += 1
            r += 1
            res = max(res, cur)
        return res