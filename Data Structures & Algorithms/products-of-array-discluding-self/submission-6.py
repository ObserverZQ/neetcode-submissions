class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # optimal: use one array to store the leftside result first and then iterate from the rightmost element to left
        n = len(nums)
        res = [1] * n
        # leftside
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        # print('res after leftside', res)
        # rightside
        rightProduct = nums[n - 1]
        for i in range(n - 2, -1, -1):
            # print('res[i]', i, res[i], res[i + 1], nums[i+1])
            res[i] = res[i] * rightProduct
            rightProduct *= nums[i]
        return res