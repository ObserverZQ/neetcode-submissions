class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        
        # my idea: move right first, and keep a set between l and r
        # if see duplicate character that r points to
        # move l by one?
        seen = set()
        lengthMax = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            # seen.add(s[r])
            # ssa
            length = r - l + 1
            # print('cur length', length, 'r', r, 'l', l)
            lengthMax = max(length, lengthMax)
        return lengthMax
