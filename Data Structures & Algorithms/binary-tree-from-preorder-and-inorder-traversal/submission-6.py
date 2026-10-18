# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: the first is the root
        # inorder: left subtree -> root -> right subtree
        # so, the first element in each segment in preorder is the middle point in the same segment in inorder
        # basecase:
        # if not preorder or not inorder:
        #     return None
        # the root is the very first element in preorder
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        # ...
        # print('inorder', inorder)
        # print('preorder', preorder)
        # rootIndexForInorder = inorder.index(rootVal)
        # optimize: use a hashmap to track value index in inorder to avoid O(n) for index()
        in_indices = { val: idx  for idx, val in enumerate(inorder) }
        self.pre_idx = 0 # track current pre_idx. basically we create roots in this order!
        def dfs(idx_left, idx_right):
            if idx_left > idx_right:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            # get the mid point(current root) in inorder
            mid = in_indices[root_val]
            root.left = dfs(idx_left, mid - 1)
            root.right = dfs(mid + 1, idx_right)
            return root
        return dfs(0, len(inorder) - 1)