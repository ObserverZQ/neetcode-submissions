# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # special cases for number 0
        if l1.val == 0 and not l1.next:
            return l2
        if l2.val == 0 and not l2.next:
            return l1

        # create a node p to store the result
        p1 = l1
        total = 0 # record the overall addition result
        prev = 0 # record the result of the previous unit addition divided by 10
        index = 0
        head = None

        while l1 and l2:
            total = l1.val + l2.val + prev
            l1 = l1.next
            l2 = l2.next
            prev = total // 10
            p1.val = total % 10
            if index == 0:
                head = p1
            temp = p1
            p1 = p1.next
            index += 1
        
        remaining = l1 or l2
        p1 = temp
        while remaining:
            total = remaining.val + prev
            prev = total // 10
            p1.next = ListNode(total % 10)
            p1 = p1.next
            remaining = remaining.next

        # check if a final 1 is needed to add as the highest unit
        if prev == 1:
            p1.next = ListNode(prev, None)
        
        return head