class Solution:
    # dynamic window size. start with r as 0, and when the window has all the characters in t,
    # shrink window by moving l to the right(l += 1)
    def minWindow(self, s: str, t: str) -> str:
        if t == '':
            return ''
        
        countT, window = {}, {}
        for chac in t:
            countT[chac] = countT.get(chac, 0) + 1 # use get() to avoid error
        
        # needed: number of distinct characters that needed to be matched
        covered, needed = 0, len(countT)

        res = [-1, -1]
        resLen = float('infinity')
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in countT and window[c] == countT[c]:
                covered += 1

            while covered == needed:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # now we shrink the left side to minimize the substring
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    covered -= 1
                l += 1
        return s[res[0] : res[1] + 1] if resLen < float('infinity') else ''

    