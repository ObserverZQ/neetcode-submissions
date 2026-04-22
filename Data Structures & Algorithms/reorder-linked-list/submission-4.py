# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None
        # use the slow/fast pointers to set slow at the middle to reverse the second half
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        temp = slow
        slow = slow.next
        temp.next = None

        while slow:
            slow.next, slow, temp = temp, slow.next, slow
        
        # when temp.next is None, we finish inserting the second half
        cur = head
        while temp.next:
            cur.next, temp.next, cur, temp = temp, cur.next, cur.next, temp.next

        return None