class Solution:
    def trap(self, height: List[int]) -> int:
        # INTUITION: the amount of water at each position (forget about the position of its left bar and right bar first), is the min of (its left bar height and its right bar height) minus its height, as its width is 1.
        length = len(height)
        l, r = 0, length - 1
        if len(height) <= 2:
            return 0
        # calculate the prefix max (highest from left side)
        prefix = [0] * length
        for i in range(1, length):
            prefix[i] = max(height[i - 1], prefix[i - 1])
        # calculate the suffix max (highest from right side)
        suffix = [0] * length
        for i in range(length - 2, -1, -1):
            suffix[i] = max(height[i + 1], suffix[i + 1])
        res = 0
        for i in range(length):
            minimum = min(prefix[i], suffix[i])
            res += (minimum - height[i]) if minimum > 0 and minimum > height[i] else 0
        # print(prefix, suffix)
        return res
