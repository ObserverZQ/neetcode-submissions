# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # recursive dfs. use closure and a helper function to keep track of depth
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(node: Optional[TreeNode], depth: int):
            if not node:
                return None
            # we just reach the next level, so we create a new sublist for the new level
            # so that res[depth] will not cause error
            if len(res) == depth:
                res.append([])
            
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return res
        