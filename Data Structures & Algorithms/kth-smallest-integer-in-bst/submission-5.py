# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # dfs recursion, in-order traversal. take a global count, stop when reached k
        count = 0
        def dfs(node: Optional[TreeNode]) -> (int, int):
            nonlocal count
            if not node:
                return None
            left = dfs(node.left)
            if left and left[0] == k:
                return left
            count += 1
            if count == k:
                return (k, node.val)
            return dfs(node.right)

        return dfs(root)[1]
                

