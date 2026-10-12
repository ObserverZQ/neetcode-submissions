class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # pwwkadsf
        l = 0
        maxLength = 0
        seen = set()

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            length = r - l + 1
            maxLength = max(maxLength, length)
        return maxLength
