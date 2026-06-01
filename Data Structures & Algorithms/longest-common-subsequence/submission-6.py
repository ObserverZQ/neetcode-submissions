class Solution:
    # bottom-up 2d dp
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        len1 = len(text1)
        len2 = len(text2)

        prev, cur = [0] * (len2 + 1), [0] * (len2 + 1)
        # dp = [[0 for j in range(len2 + 1)] for i in range(len1 + 1)]

        for i in range(len1 - 1, -1, -1):
            for j in range(len2 - 1, -1, -1):
                if text1[i] == text2[j]:
                    cur[j] = prev[j+1] + 1
                else:
                    cur[j] = max(prev[j], cur[j+1])
            cur, prev = prev, cur
        return prev[0]