# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = None, head
        if not head:
            return None
        # set fast pointer n steps ahead of slow,
        # so we have slow as the node before the node to be deleted
        # null -> 1 -> 2, n == 1
        # slow.   f
        #         s.   f n == 0
        # null -> 1 -> 2, n == 2
                       #f, n = 1
        while fast and fast.next:
            if slow:
                slow = slow.next
            fast = fast.next
            n -= 1
            if n == 0:
                slow = head
        
        if slow and slow.next: # the node to be deleted is not the first node
            slow.next = slow.next.next
        else: # the node to be deleted is the first node
            temp = head
            head = head.next
            temp.next = None
        
        return head
        # if n == 1:
        #     temp = head
        #     head = head.next
        #     temp.next = None
        #     return head