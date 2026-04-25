# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # bfs interation. time O(n), space O(n)
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        q = deque([(root, float('-inf'))]) # set negative infinity as the initial max

        while q:
            node, cur_max = q.popleft()
            if node.val >= cur_max:
                res += 1
                cur_max = node.val
            if node.left:
                q.append((node.left, cur_max))
            if node.right:
                q.append((node.right, cur_max))
        return res