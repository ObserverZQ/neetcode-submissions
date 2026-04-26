class Solution:
    # space O(1) as there are a total of 26 letters
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        letters = [0] * 26
        #  the ord() function is a built-in utility that
        # returns the integer representing the Unicode code point of a specific character
        # so letters[0] represents unicode letter a - ord('a')
        # letter[1] represents unicode letter b - ord('a'), as each letter differ by one in unicode
        for i in range(len(s)):
            letters[ord(s[i]) - ord('a')] += 1
            letters[ord(t[i]) - ord('a')] -= 1
        for count in letters:
            if count != 0:
                return False
        return True

        