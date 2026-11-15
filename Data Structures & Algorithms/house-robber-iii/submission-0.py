# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # first get the results of left and right subtree, then compare between rob this and skip this. if rob this, we can only get the results from left and right excluding themselves, otherwise we skip this and get the max results from left and right
        def dfs(node):
            if not node:
                return [0, 0]
            left = dfs(node.left)
            right = dfs(node.right)
            rob_node = node.val + left[1] + right[1]
            skip_node = max(left) + max(right)
            return [rob_node, skip_node]

        return max(dfs(root))