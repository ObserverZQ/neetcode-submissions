class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        l, r = 0, len(nums) - 1
        while l <= r:
            # # (l + r) // 2 can lead to overflow
            # mid = l + (r - l) // 2
            mid = (l + r) // 2
            '''
            nums=[-1,0,2,4,6,8]
            target=3
            l = 0, r = 5 mid = 2, 2 < 3
            l = 2, r = 5 mid = 3, 4 > 3
            l = 2, r = 3 mid = 2, 2 < 3
            '''
            # if mid == l:
            #     break
            # print(f'l: {l}, r: {r}, mid: {mid}')
            if nums[mid] == target:
                res = mid
                break
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
        return res