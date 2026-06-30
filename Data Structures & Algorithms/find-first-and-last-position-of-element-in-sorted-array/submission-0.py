class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums: List[int], target: int, searchLeft: bool):
            l, r = 0, len(nums) - 1
            i = -1
            while l <= r:
                m = l + (r - l) // 2

                if nums[m] == target:
                    i = m
                    if searchLeft:
                        r = m - 1
                    else:
                        l = m + 1
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return i
        first = binarySearch(nums, target, searchLeft = True)
        last = binarySearch(nums, target, searchLeft = False)
        return [first, last]
        