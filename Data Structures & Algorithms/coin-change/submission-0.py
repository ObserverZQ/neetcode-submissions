class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # optimal bottom-up dp, time: O(amount * len(coins)), space: O(amount)

        dp = [float('inf')] * (amount + 1) # dp[0] = 0, store all the way to dp[amount], default value amount + 1
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                # only try to update if the current coin is a valid part for the amount, meaning it is not greater than amount
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1) # +1 stands for using the coin c. min stands for using only the minimum coint amount needed for some amount like 7, which have multiple coin combinations, like 3+4, 5+1+1
        return dp[amount] if dp[amount] != float('inf') else -1