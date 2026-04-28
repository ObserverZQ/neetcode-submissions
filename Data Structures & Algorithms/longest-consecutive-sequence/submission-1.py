class Solution:
    # hash set solution. time O(n), space O(n)
    # key idea: A number is the start of a sequence if num - 1 is not in the set.
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
    '''
    neetcode version:
    numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet:
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    '''
            