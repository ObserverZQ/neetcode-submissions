class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dt = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dt:
                return [dt[diff], i]
            else:
                dt[nums[i]] = i
        return None