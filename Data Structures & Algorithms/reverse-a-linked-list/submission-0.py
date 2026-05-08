# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # recursion
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(second: Optional[ListNode], head: Optional[ListNode]) -> Optional[ListNode]:
            if not head:
                return second
            temp = head 
            head = head.next # now new head points to 3
            temp.next = second # now 2 points to 1, we get 2 -> 1
            # finally we connect 3, the new head to 2 -> 1
            return reverse(temp, head)
        if not head:
            return None
        # special case: the very head's next becomes null, so that it becomes the tail
        temp = head
        head = head.next
        temp.next = None
        # then we set the next of the head's next into the original head(reverse)
        # 1 -> 2 -> 3
        # second: 1  head: 2 -> 3
        return reverse(temp, head)

