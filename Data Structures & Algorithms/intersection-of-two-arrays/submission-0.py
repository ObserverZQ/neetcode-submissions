class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # use hashset or hashmap and remove the matched number to avoid duplicates
        # time: O(n), space: O(n)
        set1 = set(nums1)
        res = []

        for num in nums2:
            if num in set1:
                set1.remove(num)
                res.append(num)
        return res