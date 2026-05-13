# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # we merge a list(i th) with the previous(i-1) list in the array,
    # and get the head of the merged ith list, then move to the next linked list in the array  
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # a helper function that merges two lists, with O(1) space complexity
        def merge(list1: Optional[ListNode], list2: Optional[ListNode]):
            # printt(list1)
            if not list1:
                return list2
            if not list2:
                return list1
            dummy = ListNode(0) # the dummy before the head
            tail = dummy # the node used to construct the merged linkedlist
            while list1 and list2: # l1: 1 -> 3 -> 5 l2: 2 -> 4 -> 6
                if list1.val <= list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
            # add the remaining parts
            tail.next = list1 if list1 else list2
            return dummy.next

        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        head = lists[0]
        # now we have at least two linked lists
        for i in range(1, len(lists)):
            head = merge(head, lists[i])
        return head
