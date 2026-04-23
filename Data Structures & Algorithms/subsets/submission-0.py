class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # first question for backtracking
        res = []
        subset = []

        # define the helper within to use closure
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy()) # shallow copying
                return
            subset.append(nums[i])
            dfs(i+1) # recurse to next index while containing this current number
            subset.pop()
            dfs(i+1) # recurse to next index without this current number
        
        dfs(0)
        return res