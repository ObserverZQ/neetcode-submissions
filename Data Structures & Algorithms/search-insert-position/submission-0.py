class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        res = 0
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            print(f'l: {l}, r: {r}, mid: {mid}')
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
                # if insert before a numb, at the position where the nums[mid] is smaller than the current number
                res = mid
            else:
                l = mid + 1
        return l
        # if l > r:
        #     return l
        # return res
        # l = 0, r = 5 m = 2
        # l = 3, r = 5 m = 4
        # l = 3, r = 3 m = 3
        # l = 4, r = 3 break

        # l = 0, r = 5 m = 2
        # l = 3, r = 5 m = 4
        # l = 5, r = 5 m = 5
        # l = 6, r = 5 break
