class Solution:
    '''
    When there are few elements to remove, the previous approach does unnecessary copying.
Instead, we can swap unwanted elements with elements from the end of the array.
When we encounter the target value, we replace it with the last element and shrink the valid range by one.
This minimizes write operations when removals are rare.
    '''
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                n -= 1
                nums[i] = nums[n]
            else:
                i += 1
        return n