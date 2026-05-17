# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimal(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        cur = root
        while cur and cur.left:
            cur = cur.left
        return cur
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            # we are deleting the current root, check its children
            # a.for root with 0-1 children, we return the opposite subtree
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            # b. for root with 2 subtrees, we find the minimum of its right subtree
            # then set the root's value to that node's value
            # then delete that node in its original position.
            minimum = self.minimal(root.right)
            root.val = minimum.val
            root.right = self.deleteNode(root.right, minimum.val)
        return root