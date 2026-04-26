class Solution:
    # my solution: create a helper funciton to generate uni presentations for
    # anagram strings. sort the array of unicodes then convert them to string format.
    # in the main function, we store a table of uni -> str list
    # finally we print the values and use list comprehension to form the answer.
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for i in range(len(strs)):
            uni = self.getUni(strs[i])
            if uni in table:
                table[uni].append(strs[i])
            else:
                table[uni] = [strs[i]]
        return list(table.values())

    def getUni(self, s: str) -> bool:
        base = ord('a')
        res = []
        for c in s:
            res.append(ord(c) - base)
        return str(sorted(res))