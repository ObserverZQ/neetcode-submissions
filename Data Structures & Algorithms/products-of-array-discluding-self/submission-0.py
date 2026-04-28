class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        prefix = [1] * n # store the accumulative product from left to the element before nums[i]
        suffix = [1] * n # store the accumulative product from right to the element after nums[i]
        for i in range(1, n):
            # accumulate products from previous multiplication
            if i == 1:
                prefix[i] = nums[0]
            else:
                prefix[i] = prefix[i - 1] * nums[i - 1]
        # print(f'prefix: {prefix}')
        
        for i in range(n - 2, -1, -1):
            # accumulate products from previous multiplication
            if i == (n - 2):
                suffix[i] = nums[n - 1]
            else:
                suffix[i] = suffix[i + 1] * nums[i + 1]
        # print(f'suffix: {suffix}')
        for i in range(0, n):
            output[i] = prefix[i] * suffix[i]

        return output