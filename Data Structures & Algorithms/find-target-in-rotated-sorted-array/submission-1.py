class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            # 3,4,5,6,1,2 target = 1
            # the left part is sorted, so we compare the target and mid to decide check l or r part
            # a. the array has rotated over half of its length, so the target on the right part can be eigher larger than mid or smaller than left
            # b. the array is on the left, which is sorted, so we simply check the left
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]: # target = 1, check right
                    l = m + 1
                else: # target = 4, check left
                    r = m - 1
            # 6,1,2,3,4,5 the left part is not sorted
            else:
                if target < nums[m] or target > nums[r]: # target = 6, check left
                    r = m - 1
                else: # target = 4, check right
                    l = m + 1
        return -1
            

