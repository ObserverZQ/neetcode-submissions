# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def count(node: TreeNode, val_max: int) -> None:
            # decide whether the current node is a good node, 
            # based on the max val on the path is smaller than or equal to its val
            # and go to left and right subtrees
            if not node:
                return 0
            if node.val >= val_max:
                return 1 + count(node.left, node.val) + count(node.right, node.val)
            else:
                return count(node.left, val_max) + count(node.right, val_max)
        # res = count(root, float('-inf'))
        return count(root, float('-inf'))