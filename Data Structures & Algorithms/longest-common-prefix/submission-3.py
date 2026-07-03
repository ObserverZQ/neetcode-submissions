class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        i = 0
        while True:
            for j in range(len(strs)):
                if not strs[j]:
                    return res
                if i >= len(strs[j]):
                    return res
                elif res + strs[0][i] not in strs[j]:
                    return res
            res += strs[0][i]
            i += 1
        return res