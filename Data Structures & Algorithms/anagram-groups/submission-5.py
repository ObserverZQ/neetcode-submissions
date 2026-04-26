class Solution:
    # hash table solution. time O(m*n) space O(m) for extra space, O(m*n) for output
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)
        # anagram strings have the same frequency of letters in them,
        # so we can create a tuple based on a 26-digit list to put each string in strs
        # into their specific position
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            # we used defaultdict so this line works fine
            # for keys that doesn't exist in the table yet
            table[tuple(count)].append(s)
        return list(table.values())