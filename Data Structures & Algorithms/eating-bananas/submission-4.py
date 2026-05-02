class Solution:
    # time O(n * log m), space O(1)
    # n is len of piles and m is the maximum number of bananas in a pile
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        k = r
        while l <= r:
            m = l + (r - l) // 2 # the current mid point of speed ranges
            # temp = m
            hours = sum([math.ceil(float(p)/m) for p in piles])
            if hours > h:
                l = m + 1
            elif hours <= h: # meet the requirement, so we record the speed and shrink the search range
                k = m
                r = m - 1
        return k