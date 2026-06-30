class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            # e.g. nums = [3,4,5,6,1,2]
            # 1. the left half is sorted, meaning the divider is on the right, in other words,
            # the array has rotated more than half of its length after being modded
            if nums[l] <= nums[m]:
                # e.g. target = 1 or target = 6, on the right
                if nums[m] < target or nums[l] > target:
                    l = m + 1
                else:
                    r = m - 1
            # 2. the right half is sorted, nums = [6, 1, 2, 3, 4, 5]
            else:
                # e.g. target = 1 or target = 6, on the left
                if nums[m] > target or nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1
        return -1