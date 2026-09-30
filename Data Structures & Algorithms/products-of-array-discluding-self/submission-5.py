class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # optimal with space O(1)
        n = len(nums)
        res = [1] * n

        # store results from left side
        for i in range(1, n):
            res[i] = res[i - 1] * nums[i - 1]
        
        # multiply results from right side
        rightProduct = nums[n - 1]
        for i in range(n - 2, -1, -1):
            res[i] *= rightProduct
            rightProduct *= nums[i]
        
        return res