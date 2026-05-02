class Solution:
    # lower bound
    # In a rotated sorted array, the minimum element is the first element of the rotated portion.
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]: # 6 7 1 2 3 4 5 search the left half
                r = m
            else:
                # 4 5 6 7 1 2 search the right half
                l = m + 1
        return nums[l]