class Solution:
    # greedy algorithm with set-based optimization
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        if not nums:
            return res
        num_set = set(nums)
        for n in num_set:
            if n - 1 not in num_set:
                cur = 0
                temp = n
                # now temp is definitely the start of a sequence
                while temp in num_set:
                    cur += 1
                    temp += 1
                res = max(res, cur)
        return res
            