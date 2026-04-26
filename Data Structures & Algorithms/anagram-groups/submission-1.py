class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for i in range(len(strs)):
            # print(f'str: {strs[i]}')
            uni = self.getUni(strs[i])
            # print(f'str: {strs[i]}, uni: {uni}')
            if uni in table:
                table[uni].append(strs[i])
            else:
                table[uni] = [strs[i]]
        return [val for val in table.values()]

    def getUni(self, s: str) -> bool:
        base = ord('a')
        res = []
        for c in s:
            res.append(ord(c) - base)
        # if s == 'may':
        #     print('may')
        #     print(res)
        # if s == 'buy':
        #     print('buy')
        #     print(res)
        return str(sorted(res))