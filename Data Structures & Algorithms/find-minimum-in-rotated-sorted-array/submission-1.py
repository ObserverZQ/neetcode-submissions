class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            # If the current window is already sorted, update the answer with nums[left] and stop.
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            # Update the answer with nums[mid].
            m = (l + r) // 2
            res = min(res, nums[m])
            # If the left half is sorted, move search to the right half.
            if nums[m] >= nums[l]:
                l = m + 1
            else: # otherwise search the left half
                r = m - 1
        return res