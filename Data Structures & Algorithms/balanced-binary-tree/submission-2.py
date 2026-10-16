# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # as soon as we find the left and right subtree of any node differ more than 1
        # we return False.
        # after iterating the whole tree, we return True
        balanced = True
        if not root:
            return balanced
        def getHeight(node: Optional[TreeNode]):
            nonlocal balanced
            if not balanced:
                return -1
            if not node:
                return 0
            print('node', node.val)
            left_height = getHeight(node.left)
            right_height = getHeight(node.right)
            print('left height for node', node.val, ': ',left_height)
            print('right height for node', node.val, ': ',right_height)
            if left_height == -1 or right_height == -1:
                return -1
            if abs(left_height - right_height) > 1:
                balanced = False
                return -1
            return 1 + max(left_height, right_height)
        getHeight(root)
        return balanced


