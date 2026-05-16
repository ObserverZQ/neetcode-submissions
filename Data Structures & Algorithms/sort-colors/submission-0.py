class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0] * 3 # each pos records the times that pos(num) occurs in the nums
        for num in nums:
            counts[num] += 1
        i = 0
        for j in range(len(counts)): # 0, 1, 2
            for _ in range(counts[j]): # set nums' elements counts[j] times
                nums[i] = j
                i += 1
