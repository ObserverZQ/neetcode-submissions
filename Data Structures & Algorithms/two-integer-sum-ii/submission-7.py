class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                break
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                r -= 1
            # while 0 < l < len(numbers) - 1 and numbers[l] == numbers[l+1]:
            #     l += 1
            # while r > 1 and numbers[r] == numbers[r-1]:
            #     r -= 1
        if numbers[l] + numbers[r] == target:
            return [l+1, r+1]
        else:
            return []