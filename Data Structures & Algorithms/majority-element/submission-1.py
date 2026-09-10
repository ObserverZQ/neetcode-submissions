class Solution:
    # time: O(nlogn), space: O(1) or O(n) depending on the sorting algorithm
    def majorityElement(self, nums: List[int]) -> int:
        # sort, then the middle pos must be majority, bcs the amount reaches half or more than half
        nums.sort()
        return nums[len(nums) // 2]
