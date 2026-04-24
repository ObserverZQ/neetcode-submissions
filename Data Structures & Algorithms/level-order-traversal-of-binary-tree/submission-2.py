# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # iterative. use a stack to store all same-level nodes. time O(n), space O(n)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # res = []
        # if not root:
        #     return res
        # stack = [root]
        # while stack:
        #     nodes = stack[:]
        #     stack.clear()
        #     sublist = []
        #     for node in nodes:
        #         sublist.append(node.val)
        #         if node.left:
        #             stack.append(node.left)
        #         if node.right:
        #             stack.append(node.right)
        #     res.append(sublist)
        # return res

        # neetcode version
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q) # the count of nodes on the same level, including None
            level = [] # store nodes' vals on the same level
            for i in range(qLen):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res
                
        