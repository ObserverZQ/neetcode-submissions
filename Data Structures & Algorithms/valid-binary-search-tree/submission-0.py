# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], min_val: int, max_val: int) -> bool:
            # based on the regional min and max decended from ancestors
            if not node:
                return True
            # invalid condition: nodes on right subtrees are lesser than the parent
            # or nodes on left subtrees are greater than the parent
            if node.val <= min_val or node.val >= max_val:
                return False
            # now the node's val must be like min_val < node.val < max_val,
            # so we check left and right subtrees based on new boundary values
            if not dfs(node.left, min_val, node.val):
                return False
            if not dfs(node.right, node.val, max_val):
                return False
            return True

        return dfs(root, float('-inf'), float('inf'))