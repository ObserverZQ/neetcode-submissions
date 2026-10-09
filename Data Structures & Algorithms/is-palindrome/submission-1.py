class Solution:
    def isPalindrome(self, s: str) -> bool:
        # isalnum tells if a character is alphanumeric ((A-Z, a-z) and numbers (0-9).)
        # use list concatenation to remove white space, and join API to transform the list into a string
        s = ''.join(c for c in s if c.isalnum())
        s = s.lower()

        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
        