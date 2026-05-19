class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        # i: the starting index where we check the combination of nums
        # arr: the culminated array so far
        # total: the sum before the current call
        def dfs(i, arr, total):
            if total == target:
                res.append(arr.copy()) # use copy() to avoid the result being modified
                return
            if total > target or i >= len(nums):
                return
            # for each call, we can choose to add current number or not.
            arr.append(nums[i])
            dfs(i, arr, total + nums[i])
            arr.pop() # backtracking
            dfs(i + 1, arr, total)
            # backtrack
        dfs(0, [], 0)
        return res
                