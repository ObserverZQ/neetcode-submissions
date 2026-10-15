# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # we wanna start from leave, going up
        # so the diameter at each non-leaf node is the left subtree leaf path to it + the right subtree leaf path to it
        maxLength = 0
        # how do we go upwards?
        # use recursion to get the depth of its subtree nodes first,then get the sum to update globalMax
        # so the helper function need to return current tree's height
        def dfs(node):
            nonlocal maxLength
            if not node:
                return 0
            left_height = dfs(node.left)
            right_height = dfs(node.right)
            maxLength = max(maxLength, left_height + right_height)
            return 1 + max(left_height, right_height)

        dfs(root)
        return maxLength        
