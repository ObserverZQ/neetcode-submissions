# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(node: Optional[TreeNode], sub: Optional[TreeNode]) -> root:
            if not node and not sub:
                return True
            if not node or not sub:
                return False
            return node.val == sub.val and isSameTree(node.left, sub.left) and isSameTree(node.right, sub.right)

        if not root and not subRoot:
                return True
        if not root or not subRoot:
            return False
        if isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
