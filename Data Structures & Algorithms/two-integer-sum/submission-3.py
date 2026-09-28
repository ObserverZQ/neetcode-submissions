class Solution:
    # HashMap one pass. time: O(n), space: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = dict() # or {}
        for k in range(len(nums)):
            diff = target - nums[k]
            if diff in numMap:
                return [numMap[diff], k]
            numMap[nums[k]] = k
        