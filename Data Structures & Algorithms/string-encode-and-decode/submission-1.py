class Solution:
    # the problem here is to create a sep to distinguish between different elements in the array.
    # we can't use sth like a comma as there could be commas in the strings
    # how can we make the sep unique to each string?
    # using each string's length helps.
    # with the number at the start of each string after they are encoded, we can cut the string into list making sure each string is the same as the input.
    def encode(self, strs: List[str]) -> str:
        res = ''
        for string in strs:
            length = len(string)
            res += str(length) + '#' + string
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i + 1
            # use j to record the pos of #
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            j += 1
            res.append(s[j:j+length])
            i = j + length
        return res
