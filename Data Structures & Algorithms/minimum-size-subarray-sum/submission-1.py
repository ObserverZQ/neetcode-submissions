class Solution:
    # sliding window, time: O(n), space: O(1)
    # notice the inner while loop does not execute n times for every r iteration.
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        length = float('inf')

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                length = min(length, r - l + 1)
                total -= nums[l]
                l += 1
        
        return length if length < float('inf') else 0
            
            