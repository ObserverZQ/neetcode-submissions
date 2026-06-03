class Solution:
    # kadane's algorithm, time: O(n), space: O(1)
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        globalMax, globalMin = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for n in nums:
            # shortened version of curMax = max(curMax, 0), curMax += n
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            total += n
            globalMax = max(curMax, globalMax)
            globalMin = min(curMin, globalMin)

        # globalMax is a subarray in the middle, while total - globalMin gives us a tail-head subarray
        return max(globalMax, total - globalMin) if globalMax > 0 else globalMax
                