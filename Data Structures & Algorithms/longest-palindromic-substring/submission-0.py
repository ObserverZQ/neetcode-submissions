class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        # 2. 2-D dynamic programming
         # O(n2) for time, O(n2) for space
        # index = 0
        # maxLen = 1
        # res = ''
        # n = len(s)
        # dp = [[False] * n for _ in range(n)]

        # for i in range(n-1, -1, -1):
        #     for j in range(i, n):
        #         # check palindrome, where i, j are next to each other.
        #         # or j is at least two letters away from i but their center substring is palindrome
        #         if s[i] == s[j] and (j - i <= 2 or dp[i+1][j-1]):
        #             dp[i][j] = True

        #             if (j - i + 1) > maxLen:
        #                 maxLen = j - i + 1
        #                 index = i
    
        # return s[index: index + maxLen]

        # 3. two pointers, check odd and even substrings with every index as the center
        # O(n2) for time, O(1) for space
        index = 0
        maxLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxLen = r - l + 1
                    index = l
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxLen = r - l + 1
                    index = l
                l -= 1
                r += 1
        return s[index : index + maxLen]