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

        # i: starting index of the substring, j: end index of the substring
        def dfs(i, j):
            # 1. check whether finished building all substrings
            # when j reaches the end, we have built all valid substrings across all indices,
            # so no more characters needed to be examined
            if j >= len(s):
                # corresponds to dfs(j+1, j+1) below, which means the upper level calls are all valid palindromes
                if i == j:
                    res.append(part.copy())
                return
            
            # 2. still in the middle, so check if the current substring is palindrome
            # and keep exploring the remaining pieces
            if isPalindrome(s, i, j):
                part.append(s[i : j + 1])
                dfs(j + 1, j + 1)
                part.pop() # backtrack
            
            # 3. done checking [i, j] substring(palindrome or not), try moving j further
            dfs(i, j+1)
        
        dfs(0, 0)
        return res