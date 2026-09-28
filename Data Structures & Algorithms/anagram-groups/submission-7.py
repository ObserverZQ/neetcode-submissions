class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # problem no flow map
        # sort every word to see if it is in a sorted word map?
        res = []
        wordMap = {}
        for word in strs:
            # python grammar
            copy = word
            copy = ''.join(sorted(copy))
            if copy in wordMap:
                wordMap[copy].append(word)
            else:
                wordMap[copy] = [word]
        for key in wordMap:
            res.append(wordMap[key])
        return res