class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # boyer-moor voting algorithm,
        # which keeps a candidate and a count, which gets incremented/decremented depends on the current element
        res = 0
        count = 0
        # 2 3 4 4 1 1 1
        for num in nums:
            if count == 0:
                res = num
                count = 1
                continue
            if num == res:
                count += 1
            else:
                count -= 1
        return res