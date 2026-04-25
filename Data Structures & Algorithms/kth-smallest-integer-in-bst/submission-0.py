# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # let's try dfs recursive left -> node -> right to traverse the entire tree
        # from the smallest value and pass an int to check it with k
        arr = []
        def dfs(node: Optional[TreeNode]) -> None:
            # first get the left subtrees, then the node itself, then right subtrees
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)

        return arr[k - 1]