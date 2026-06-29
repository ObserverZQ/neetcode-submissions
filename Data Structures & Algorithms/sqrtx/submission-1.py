class Solution:
    def mySqrt(self, x: int) -> int:
        l = 0
        r = x
        res = 0

        while l <= r:
            mid = l + (r - l) // 2
            print(f'l: {l}, r: {r}, mid: {mid}')
            if mid ** 2 > x:
                r = mid - 1
            elif mid ** 2 < x: ## record the smaller sqrt for rounding down 
                l = mid + 1
                res = mid
            else:
                return mid
        return res