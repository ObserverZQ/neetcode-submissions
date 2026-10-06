class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # each group have identical count for each letter, so we can create a map with the 26-letter frequency as tuple as the key, and store the exact words as arrays as the value. finally we output the values of the map as a list.
        groups = defaultdict(list) # here we set the default value of each key an empty list
        for word in strs:
            key = [0] * 26 # store the freq of each letter, their indices being their unicode minus the letter 'a'
            for c in word:
                key[ord(c) - ord('a')] += 1
            groups[tuple(key)].append(word)
        # print('groups', groups)
        return list(groups.values())
