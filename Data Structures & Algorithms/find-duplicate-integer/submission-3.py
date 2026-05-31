class Solution:
    # view the value on each index as the pointer to the next node in the linked list.
    # time O(n) space O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]] # two steps forward

            # we found a cycle where slow meets fast
            # now slow is in the cycle
            if slow == fast:
                break
        # initiate another pointer from the start
        # when slow2 and slow meet again, where they jump from has the duplicate value
        # which is their current location
        slow2 = 0 
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow2 == slow:
                return slow