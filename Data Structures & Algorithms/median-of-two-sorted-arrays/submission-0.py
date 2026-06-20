class Solution:
    # two pointers. time: O(m+n), space: O(1)
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1, len2 = len(nums1), len(nums2)
        i = j = 0
        med1 = med2 = 0

        for count in range(0, (len1 + len2) // 2 + 1):
            med2 = med1
            if i < len1 and j < len2:
                if nums1[i] <= nums2[j]:
                    med1 = nums1[i]
                    i += 1
                else:
                    med1 = nums2[j]
                    j += 1
            elif i < len1:
                med1 = nums1[i]
                i += 1
            # the only remaining case is i >= len1 and j < len2
            else:
                med1 = nums2[j]
                j += 1
        
        # if m + n is even, med1 is the second median, med2 is the first
        if (len1 + len2) % 2 == 0:
            return float(med1 + med2) / 2
        # otherwise, med1 is the very middle position number
        else:
            return float(med1)