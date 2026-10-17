# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # a list of lists, where each list of nodes are on the same level
        # use bfs would solve this
        if not root:
            return []
        queue = deque([root])
        res = []
        while True:
            same_level_nodes = []
            queue2 = deque([])
            while len(queue):
                node = queue.popleft()
                same_level_nodes.append(node.val)
                if node.left:
                    queue2.append(node.left)
                if node.right:
                    queue2.append(node.right)
            res.append(same_level_nodes)
            if len(queue2) == 0:
                break
            queue2, queue = queue, queue2
        return res