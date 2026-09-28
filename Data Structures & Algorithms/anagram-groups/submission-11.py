class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # optimal using tuple recording the frequency of each chac
        # time: O(m * n), space: O(n)
        res = defaultdict(list)
        for s in strs:
            chacArr = [0] * 26
            for c in s:
                # ord returns the Unicode number for a single character. vice versa: chr.
                chacArr[ord(c) - ord('a')] += 1
            res[tuple(chacArr)].append(s)
        return list(res.values())