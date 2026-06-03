class Solution:
    # sliding window
    # time: O(n), space: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]
        L = 0

        for R in range(len(nums)):
            if curSum < 0:
                curSum = 0
                L = R
            curSum += nums[R]
            maxSum = max(maxSum, curSum)

        return maxSum