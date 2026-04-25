# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # hashmap + dfs. time: optimized from O(n2) to O(n)(saved the mid = inorder.index(preorder[0]))
    # space O(n)
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # the first node in the preorder list is the root
        # the left part of the inorder list is left subtree, while the right part is right subtree
        indices = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0 # track the index of the current targeting preorder element

        def dfs(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None

            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            root.left = dfs(l, mid - 1)
            root.right = dfs(mid + 1, r)
            return root

        return dfs(0, len(inorder) - 1) 

