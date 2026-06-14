class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        curSet = []

        def backtrack(i, curSet):
            if i >= len(nums):
                res.append(curSet.copy())
                return
            curSet.append(nums[i])
            backtrack(i+1, curSet)
            curSet.remove(nums[i])
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            backtrack(i+1, curSet)
        
        backtrack(0, curSet)
        
        return res