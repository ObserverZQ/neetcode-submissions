class Solution:
    # bottom-up 2d dp
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        len1 = len(text1)
        len2 = len(text2)

        dp = [[0 for j in range(len2 + 1)] for i in range(len1 + 1)]

        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]