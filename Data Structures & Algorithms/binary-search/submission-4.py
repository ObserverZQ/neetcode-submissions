class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            # # (l + r) // 2 can lead to overflow in In languages using 32-bit signed integers (int) like Java and C++
            # mid = l + (r - l) // 2
            mid = (l + r) // 2
            '''
            nums=[-1,0,2,4,6,8]
            target=3
            l = 0, r = 5 mid = 2, 2 < 3
            l = 3, r = 5 mid = 4, 6 > 3
            l = 3, r = 3 mid = 3, 4 > 3
            l = 3, r = 2 break
            '''
            if nums[mid] == target:
                res = mid
                break
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        return res