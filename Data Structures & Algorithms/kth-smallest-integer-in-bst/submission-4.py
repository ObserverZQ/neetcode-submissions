# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # optimal recursive dfs, time O(h+k)(worst n),
    # space O(h) for recursion stack(worst n)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = k
        res = root.val

        def dfs(node: Optinal[TreeNode]) -> None:
            # Explicitly declare cnt and res are from the outer scope
            # the nonlocal keyword is used within nested functions
            # to modify variables defined in the nearest enclosing scope that are not global.
            # if we dont declare them this way we would get an error:
            # UnboundLocalError: cannot access local variable 'cnt' where it is not associated with a value
            nonlocal cnt, res
            if not node:
                return
            dfs(node.left)
            if cnt == 0:
                return
            cnt -= 1
            if cnt == 0:
                res = node.val
                return
            dfs(node.right)

        dfs(root)
        return res