class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = 0
        # contraint: no ajacent houses
        for i in range(len(nums)):
            # rob this house + the sum of house i - 2
            # do not rob this house, inherit the sum of house i - 1
            cur = max(prev2 + nums[i], prev1)
            prev2 = prev1
            prev1 = cur
        return prev1