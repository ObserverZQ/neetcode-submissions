# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def findPath(node: TreeNode, target: TreeNode, path: list) -> bool:
            # reach the end yet not found the target, so it is not a valid path
            if not node:
                return False
            path.append(node)
            if node.val == target.val:
                return True
            # check if its subtree is on the path to the target. if true, it is an ancestor for sure
            if findPath(node.left, target, path) or findPath(node.right, target, path):
                return True
            # it is not an ancestor, pop it out of the path, backtrack
            path.pop()
            return False
        path_p = []
        path_q = []
        findPath(root, p, path_p)
        findPath(root, q, path_q)

        lca = None
        # iterate the ancestors of the lesser one
        for i in range(min(len(path_p), len(path_q))):
            if path_p[i].val == path_q[i].val:
                lca = path_p[i]
            else:
                break
        return lca
        

        