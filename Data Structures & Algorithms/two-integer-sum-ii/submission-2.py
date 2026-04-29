class Solution:
    # two pointers. move l if sum is too small, and r if sum is too large.
    # time O(n), space O(1)
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        total = 0
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                break
            elif total > target:
                r -= 1
            else:
                l += 1

        if total == target:
            return [l+1, r+1]
        else:
            return []