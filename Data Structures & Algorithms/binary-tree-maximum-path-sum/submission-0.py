# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = root.val

        # return the max downward path starting from the node
        # update global max path through this node
        def calculate(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            leftMax = calculate(node.left)
            rightMax = calculate(node.right)
            leftMax = max(leftMax, 0) # avoid adding negative sums
            rightMax = max(rightMax, 0) # and make sure the total is always greater or equal to the downward path
            total = leftMax + rightMax + node.val
            if total > self.maxSum:
                self.maxSum = total
            return node.val + max(leftMax, rightMax)
        calculate(root)
        return self.maxSum