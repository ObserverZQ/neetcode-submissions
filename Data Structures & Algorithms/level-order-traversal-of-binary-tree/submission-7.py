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
        def printt(queue):
            string = ''
            for i in range(len(queue)):
                string += str(queue[i].val)
                string += ','
            
        if not root:
            return []
        queue = deque([root])
        res = []
        while True:
            same_level_nodes = []
            queue2 = deque([])
            while len(queue):
                node = queue.popleft()
                # print('node', node.val)
                same_level_nodes.append(node.val)
                # print('same_level_nodes', same_level_nodes)
                if node.left:
                    queue2.append(node.left)
                if node.right:
                    queue2.append(node.right)
            # print('queue2')
            printt(queue2)
            res.append(same_level_nodes)
            if len(queue2) == 0:
                break
            queue2, queue = queue, queue2
        return res