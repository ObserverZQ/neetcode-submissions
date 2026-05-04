class Solution:
    '''
    Instead of using extra space, we can overwrite unwanted elements in place.
We use a write pointer k that tracks where the next valid element should go.
As we scan through the array, whenever we find an element that is not equal to val, we write it at position k and move k forward.
At the end, everything before index k contains valid elements.
    '''
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k