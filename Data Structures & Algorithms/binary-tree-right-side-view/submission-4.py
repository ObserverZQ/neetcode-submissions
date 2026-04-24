# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # dfs recursive solution. looking at right first then left,
    # in every depth we add the first node we see into the res list.
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node: Optional[TreeNode], depth: int) -> None:
            if not node:
                return None
            # when we reach next level, we have exactly len elements in the res
            if len(res) == depth: # say on depth 1, before adding, we have 1 element
                res.append(node.val)
            dfs(node.right, depth + 1) # calling right first make sure we always get right first if right is not None
            dfs(node.left, depth + 1) # otherwise we can view the left from right
        dfs(root, 0)
        return res