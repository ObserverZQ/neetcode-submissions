# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # check all subtrees of root, compare with subRoot.
        # if root and subRoot are the same, it is also true
        def dfs(node: Optional[TreeNode], sub: Optional[TreeNode], subIsRoot: bool):
            if not node and not sub:
                return True
            if not node or not sub:
                return False
            print('root: ', node.val, 'subRoot: ', sub.val)
            if node.val == sub.val:
                # possible subTree start
                left_same = dfs(node.left, sub.left, False)
                right_same = dfs(node.right, sub.right, False)
                if left_same and right_same:
                    return True
            if not subIsRoot:
                return False        
            return dfs(node.left, sub, True) or dfs(node.right, sub, True)
        return dfs(root, subRoot, True)