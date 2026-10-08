class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        group = set(nums)
        # for n in nums:
        #     group.add(n)
        maxLength = 0
        length = 0
        # print('group', group)
        # look for the start of a sequence, meaning n-1 does not exit in the set
        for n in group:
            if (n - 1) not in group:
                length = 1
                # print('start', n + length)
                while (n + length) in group:
                    length += 1
                    # print('now', n + length, (n + length) in group)
                # print('length after an inner loop', length)
                maxLength = max(length, maxLength)
        return maxLength