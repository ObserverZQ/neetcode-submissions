# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # time: O(n), space: O(n)
        def dfs(node: Optional[TreeNode], minimum: int, maximum: int):
            if not node:
                return True
            # print('node.val: ', node.val, 'minimum: ', minimum, 'maximum: ', maximum)
            if node.val <= minimum or node.val >= maximum:
                return False
            if not node.left and not node.right:
                return True
            return dfs(node.left, minimum, node.val) and dfs(node.right, node.val, maximum)

        return dfs(root, float('-inf'), float('inf'))