class Solution:
    def rob(self, nums: List[int]) -> int:
        def count(first: bool) -> int:
            if len(nums) == 1:
                return nums[0]
            prev1 = 0
            prev2 = 0

            for i, n in enumerate(nums):
                if i == 0:
                    if not first:
                        continue
                if i == (len(nums) - 1):
                    if first:
                        break
                cur = max(prev1, n + prev2)
                prev2 = prev1
                prev1 = cur
            # print(f'first: {first}, prev1: {prev1}')
            return prev1
        withFirst = count(True)
        withoutFirst = count(False)
        return max(withFirst, withoutFirst)