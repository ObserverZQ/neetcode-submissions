# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
            if not head:
                return None
            
            f = head
            count = 0
            while count < k and f:
                f = f.next
                count += 1
            
            if count == k: # now f points to the first node of next group
                f = reverse(f)
                while count > 0:
                    temp = head.next
                    head.next = f
                    f = head
                    head = temp
                    count -= 1
                head = f
            return head

        return reverse(head)