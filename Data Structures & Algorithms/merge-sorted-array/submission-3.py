class Solution:
    # three pointers without extra space, space O(1)
    # by starting at last and copy the larger one at the current,
    # we can put nums2 in correct positions without copying m elements in nums1
    # contrary to putting smaller or equal elements in nums1 first,
    # we put nums1 element in the cur only when it is larger
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        cur = m + n - 1
        i, j = m - 1, n - 1
        # make sure we copy all elements in nums2
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]: # only when nums1 still have elements to iterate and it is larger
                nums1[cur] = nums1[i]
                i -= 1
            else:
                nums1[cur] = nums2[j] # this way we make sure the right part is always later
                j -= 1
            cur -= 1
            
            