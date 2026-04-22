"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.map = {}

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 1. recursion + hashmap(user-defined classes can be key in dict)
        # 1.a deep copy the original linked list, and create a map pairing original nodes and created codes
        if not head:
            return None
        
        # make sure the copy only happens once for each node
        if head in self.map:
            return self.map[head]
        
        node = Node(head.val)
        self.map[head] = node
        # use recursion to set and copy the next node
        node.next = self.copyRandomList(head.next)
        # notice this line will execute after the entire linked list has been copied(Line 27), so node.random will get assigned correctly
        # dict.get() is used to retrieve the value for a specific key without risking a KeyError if the key is missing. 
        node.random = self.map.get(head.random)

        return node
        