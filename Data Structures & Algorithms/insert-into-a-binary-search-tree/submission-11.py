# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur, tmp = root, root
        if not root:
            return TreeNode(val)
        greater = False
        while cur:
            tmp = cur
            if val > cur.val:
                greater = True
                cur = cur.right
            elif val < cur.val:
                greater = False
                cur = cur.left
        node = TreeNode(val)
        if tmp.val < val:
            tmp.right = node
        else:
            tmp.left = node
        return root

