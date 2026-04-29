class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        # find j, k pairs that satisfy -nums[i] = nums[j] + nums[k]
        # where -nums[i] is the target
        for i, num in enumerate(nums):
            # If a > 0, break (all remaining numbers are positive, so their sum is positive, not what we want).
            if num > 0:
                break

            # avoid duplicate
            if i > 0 and num == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1
            while l < r:
                total = num+nums[l]+nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1 # skip equal left numbers to avoid duplicate
        return res
