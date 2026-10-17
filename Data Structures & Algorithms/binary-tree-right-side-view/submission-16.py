# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # go through each level, add the last element on that level
        # time: O(n), space: O(h)
        # to optimize, use a variable to update it on the same level, in the last update we naturally get the rightmost node
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            len_q = len(queue)
            rightmost = None
            for i in range(len_q):
                node = queue.popleft()
                rightmost = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(rightmost)
        return res