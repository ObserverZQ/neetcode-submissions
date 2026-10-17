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
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            len_q = len(queue)
            nodes = []
            for i in range(len_q):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                nodes.append(node.val)
            res.append(nodes[len(nodes) - 1])
        return res