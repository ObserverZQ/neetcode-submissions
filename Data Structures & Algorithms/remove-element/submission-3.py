class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        k = 0
        slow, fast = 0, 0
        while slow < n and fast < n:
            if nums[slow] != val:
                k += 1
            else:
                while fast < n and nums[fast] == val:
                    fast += 1
                if fast == n:
                    break
                # exchange elements so that [val] is put into a later position
                nums[slow], nums[fast] = nums[fast], nums[slow]
                k += 1
            slow += 1
            fast += 1
        return k