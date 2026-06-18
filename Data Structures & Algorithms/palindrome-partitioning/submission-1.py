class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(sub, l, r):
            while l < r:
                if sub[l] != sub[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        res, part = [], []

        # i: starting index of the substring
        def dfs(i):
            # 1. check whether finished building all substrings
            # when j reaches the end, we have built all valid substrings across all indices,
            # so no more characters needed to be examined
            if i >= len(s):
                # all previous i-1 calss are valid palindromes, add it
                res.append(part.copy())
                return
            
            # check every index starting from i to check palindrome,
            # and proceed if cur is palindrome.
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    part.append(s[i : j + 1])
                    # explore the next slice of subtring
                    dfs(j + 1)
                    part.pop() # backtrack
        dfs(0)
        return res