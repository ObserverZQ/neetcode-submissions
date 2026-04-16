# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def getStr(node: Optional[TreeNode]) -> str:
            # pre-order traversal
            if not node:
                return '#'
            left = getStr(node.left)
            right = getStr(node.right)
            return '|' + str(node.val) + '|' + left + right
        rootStr = getStr(root)
        subRootStr = getStr(subRoot)
        return subRootStr in rootStr