class Solution:
    # kadane's algorithm.
    # time: O(n), space: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = 0
        maxSum = nums[0]

        for n in nums:
            curSum = max(curSum, 0) + n
            maxSum = max(maxSum, curSum)
        
        return maxSum