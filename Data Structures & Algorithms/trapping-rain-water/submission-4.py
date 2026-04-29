class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        res = 0
        l, r = 0, len(height) - 1
        lMax, rMax = height[l], height[r]
        while l < r:
            # the lower bar is on the left, so we accumulate areas
            # by counting the diff between left bar and cur bar heights
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                res += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                res += rMax - height[r]
        return res
