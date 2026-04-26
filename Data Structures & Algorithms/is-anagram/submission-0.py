class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        smap = {}
        for chac in s:
            smap[chac] = smap.get(chac, 0) + 1
        for chac in t:
            if chac not in smap:
                return False
            else:
                smap[chac] -= 1
                if smap[chac] == 0:
                    smap.pop(chac)
        return not smap
            