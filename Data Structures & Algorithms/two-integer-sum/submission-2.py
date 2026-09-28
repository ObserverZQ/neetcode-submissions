class Solution:
    # HashMap one pass. time: O(n), space: O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, 0
        numMap = dict()
        for k in range(len(nums)):
            diff = target - nums[k]
            if diff in numMap:
                return [numMap[diff], k]
            numMap[nums[k]] = k
        