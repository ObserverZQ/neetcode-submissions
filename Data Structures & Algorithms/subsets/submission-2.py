class Solution:
    # iteration. for every element, we add it to existing subsets to create a bunch of new subets and add them to the overall result
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for num in nums:
            # original_subsets = 
            # subsets = list(map(lambda x: x+[num], res))
            # res += subsets
            # neetcode code:
            res += [subset + [num] for subset in res]
        return res