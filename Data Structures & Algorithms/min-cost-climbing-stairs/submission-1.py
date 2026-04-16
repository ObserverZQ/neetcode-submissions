class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0] * (n + 1) # dp[n] == 0 as the nth step is the top
        dp[n - 1] = cost[n - 1]
        for i in range(n - 2, -1, -1): # notice the -1 boundary is excluded
            # we break this problem into the sub-problem:
            # the overall cost starting from ith step is:
            # its cost plus the minimum between the overall costs of its next step and its next's next step
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])
        return min(dp[0], dp[1])
