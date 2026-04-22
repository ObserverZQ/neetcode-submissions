"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # collections.defaultdict is a subclass of the built-in dict class.
        # defaultdict(lambda: "default"): Returns a custom string or value/Object.

        # comparing to solution 2 where we pass the list twice,
        # this allows us to make correct pointer connections on the spot and modify their val later.
        oldToNew = collections.defaultdict(lambda: Node(0))
        oldToNew[None] = None # !!important, for next/random pointers that point to a null
        cur = head
        while cur:
            oldToNew[cur].val = cur.val
            oldToNew[cur].next = oldToNew[cur.next] # point to a specific initialized node
            oldToNew[cur].random = oldToNew[cur.random]
            cur = cur.next
        return oldToNew[head]
