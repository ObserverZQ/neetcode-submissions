class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # my idea: the three indices have to be different.
        # use a pointer i for index i,
        # search for -nums[i] = nums[j] + nums[k], where j and k dont' overlap
        # after sorting, we select an i, then iterate from left and right with two pointers. we move j to the right when the sum is less than -num[i], or move k to the left when the sum is greater than num[k]
        i, j, k = 0, 1, len(nums) - 1
        res = []
        nums.sort()

        while i < len(nums) - 2:
            target = -nums[i]
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if (nums[j] + nums[k]) == target:
                    res.append([nums[i], nums[j], nums[k]])
                    # critical: don't just break,
                    # as there may be other j,k pairs that sum up to -nums[i]
                    j += 1
                    k -= 1
                    # avoid duplicate j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif (nums[j] + nums[k]) < target:
                    j += 1
                else:
                    k -= 1
            # make sure to increase i for outer loop
            i += 1
            # the loop here is to skip duplicate i
            while nums[i - 1] == nums[i] and i < len(nums) - 1:
                i += 1
        return res