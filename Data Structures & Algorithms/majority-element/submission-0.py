class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sort, then the middle pos must be majority, bcs the amount reaches half or more than half
        nums.sort()
        return nums[len(nums) // 2]