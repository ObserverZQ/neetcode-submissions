class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        table = {}
        n = len(nums)
        for num in nums:
            table[num] = True
        
        count = 0
        countMax = 0
        for num in nums:
            # select a start
            minus = num - 1
            if minus not in table:
                cur, start = num, num
                while cur in table:
                    cur += 1
                count = cur - start
                if countMax < count:
                    countMax = count
            else:
                continue
        return countMax
            