class Solution:
    def numDecodings(self, s: str) -> int:
        # 1D DP
        if not s or s[0] == '0':
            return 0
        # number of ways to decode s[0:i], so the current i doesn't count into the judgement
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, len(s) + 1):
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2] # the last two digits can be encoded, so the total add the total at i - 2
        return dp[-1]