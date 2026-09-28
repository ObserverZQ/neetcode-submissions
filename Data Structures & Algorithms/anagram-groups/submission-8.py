class Solution:
    # hashmap + sorting. time: O(n * mlogm) space: O(n*m)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # problem no flow map
        # sort every word to see if it is in a sorted word map?
        res = [] # a better grammar usage: res = defaultdict(list)
        wordMap = {}
        for word in strs:
            # python grammar
            copy = word # sortedS = ''.join(sorted(s))
            copy = ''.join(sorted(copy))
            if copy in wordMap:
                wordMap[copy].append(word) # res[sortedS].append(s)
            else:
                wordMap[copy] = [word]
        for key in wordMap:
            res.append(wordMap[key])
        return res # list(res.values()), as res.values() is a dict_values object