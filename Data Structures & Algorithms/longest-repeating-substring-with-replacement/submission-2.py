class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # freq most characters. replace others with that character.
        # sliding window. when replacement needs more than k, shirnk the left
        chacs = set(s)
        res = 0

        for c in chacs:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1
                
                while (r - l + 1) - count > k:
                    if s[l] == c:
                        count -= 1
                    l += 1
                
                # now we have a window whose number of replacement to get a substring full of c is less than k
                res = max(res, r - l + 1)
        return res
        