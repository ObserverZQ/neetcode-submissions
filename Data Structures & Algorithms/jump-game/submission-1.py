class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            # reachable, we go to the previous index and repeat
            if i + nums[i] >= target:
                target = i
        return target == 0
            
        