class Solution:
    # test: 1, 1, 1, 2, 2, 3
    # 1, 1, 2, 2, 2, 3
    # 1, 1, 2, 2, 3, 3
    def removeDuplicates(self, nums: List[int]) -> int:
        l = r = 0
        for r in range(len(nums)):
            if l < 2 or nums[r] > nums[l - 2]:
                nums[l] = nums[r]
                l += 1
        return l