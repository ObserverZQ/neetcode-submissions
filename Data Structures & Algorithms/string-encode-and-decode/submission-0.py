class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += (str(len(s)) + '#' + s)
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            hashtag = s.index('#')
            cnt = int(s[ : hashtag])
            string = s[ hashtag+1 : hashtag+1+cnt ]
            res.append(string)
            s = s[ hashtag+1+cnt : ]
        return res