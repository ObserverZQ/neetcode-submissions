class Solution:
    # two pointers. we simply compare r with r - 1 in a single loop, and copy r value to l
    # when we find unique values.
    # time: O(n), space: O(1)
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l