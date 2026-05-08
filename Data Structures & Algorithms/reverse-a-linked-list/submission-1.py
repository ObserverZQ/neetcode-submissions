# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # iteration
    # We walk through the list from left to right, and for each node,
    # we redirect its next pointer to point to the node behind it.
    # time O(n) space O(1)
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        # in each loop we operate on 3 nodes, 1 before, 1 cur, and 1 next
        # so that we can make sure the last node points back to its previous node
        while curr:
            temp = curr.next # get the next node of the cur
            curr.next = prev # set cur's next to its previous node
            prev = curr # set prev as cur
            curr = temp # set cur as next node
        return prev