class Solution:
    def findMin(self, nums: List[int]) -> int:
        # the key of this question is
        # to find the mid/starting point of the rotated array
        # how do we get to know that?
        # we know that in a unrotated sorted array, nums[l] <= nums[mid] <= nums[l]
        # so lets use mid/l to locate the starting point, which is the global min
        n = len(nums)
        l, r = 0, n - 1
        minIndex = 0
        # 3 4 5 6 1 2, nl = 3, nr = 2, nm = 5 => l = 3, r = 5, m =4 nm = 1
        # 4 5 6 7 nl = 4 nr = 7 nm = 5 => r = 0
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] <= nums[(m-1)%n] and nums[m] < nums[(m+1)%n]:
                return nums[m]
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return nums[minIndex]