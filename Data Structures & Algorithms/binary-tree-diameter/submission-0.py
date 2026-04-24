# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global_max = [0]
        def calculate(node: Optional[TreeNode]) -> None:
            if not node:
                return 0
            left = calculate(node.left)
            right = calculate(node.right)
            cur = left + right
            if cur > global_max[0]:
                global_max[0] = cur
            return 1 + max(left, right)
        calculate(root)
        return global_max[0]
        