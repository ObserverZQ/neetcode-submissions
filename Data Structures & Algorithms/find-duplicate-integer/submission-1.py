class Solution:
    # view the value on each index as the pointer to the next node in the linked list.
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # two steps forward

            # we found a cycle where slow meets fast
            if slow == fast:
                break

        slow2 = 0 # initiate another pointer from the start
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow2 == slow:
                return slow