class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 2D DP
        # use a dp[i][j] to record the longest palindromic subsequence in s[i:j+1], from index i to index j
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # base case
        for i in range(n):
            dp[i][i] = 1

        # fill table: consider substrings of increasing length
        for length in range(2, n + 1):
            for i in range(n - length + 1): # the largest index where we can start checking the subsequence of length length, so j wont exceed
                j = i + length - 1
                if s[i] == s[j]: # same letter at i and j, so we can add 2 to the prev subsequence
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][n-1]
