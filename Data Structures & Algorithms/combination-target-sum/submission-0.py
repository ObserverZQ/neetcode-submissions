class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        # i: the starting index where we check the combination of nums
        # cur: the culminated array so far
        # total: the sum before the current call
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                cur.append(nums[j])
                dfs(j, cur, total + nums[j])
                # we have reached the target or exceeded the target, so drop the cur's last added element
                cur.pop()
        dfs(0, [], 0)
        return res
                