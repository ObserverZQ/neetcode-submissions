class Solution:
    def rob(self, nums: List[int]) -> int:
        sums = []
        # globalMax = 0
        # contraint: no ajacent houses
        for i in range(len(nums)):
            # rob this house + the sum of house i - 2
            # do not rob this house, inherit the sum of house i - 1
            if i == 0:
                sums.append(nums[i])
            elif i == 1:
                sums.append(max(sums[i - 1], nums[i]))
            else:
                sums.append(max(sums[i - 1], sums[i - 2] + nums[i]))
        return sums[-1]