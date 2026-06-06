class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix = []
        postfix = deque([])
        total = 0
        for n in nums:
            total += n
            prefix.append(total)
        total = 0
        for i in range(len(nums) - 1, -1, -1):
            total += nums[i]
            postfix.appendleft(total)
        # print(f'prefix: {prefix}, postfix: {postfix}')
        k = 0
        while k < len(nums):
            preSum = prefix[k - 1] if k > 0 else 0
            postSum = postfix[k + 1] if (k + 1) < len(nums) else 0
            if preSum == postSum:
                return k
            k += 1
        return -1