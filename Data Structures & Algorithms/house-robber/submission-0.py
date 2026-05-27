class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [-1] * len(nums) # save the maximum $ from house i

        def dfs(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            # choose between taking the next house or the current house and the next's next house
            memo[i] = max(dfs(i+1), nums[i] + dfs(i+2))
            return memo[i]
        return dfs(0)
