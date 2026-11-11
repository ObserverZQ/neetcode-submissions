class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # for every element, we add the element to the previous accumulated subsets
        res = [[]]
        for num in nums:
            res += [subset + [num] for subset in res]
        return res