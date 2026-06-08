# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # idea: use fast and slow pointers to reverse the second half of the list
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # now slow is at the second middle node
        # e.g. 0 -> 1 -> 2 -> 3, slow is at 2
        # now we use another pointer temp to flip the second half as slow progresses to the end
        temp = None
        while slow:
            temp, slow.next, slow = slow, temp, slow.next
        # now we have 0 -> 1 -> 2 <- 3
        globalMax = 0
        while temp:
            globalMax = max(globalMax, head.val + temp.val)
            temp = temp.next
            head =  head.next
        return globalMax
