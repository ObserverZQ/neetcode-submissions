class Solution:
    # time O(n * log m), space O(1)
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort(reverse = True)
        # print(piles)
        l, r, k = 1, piles[0], piles[0]

        while l <= r:
            m = l + (r - l) // 2 # the current mid point of speed ranges
            # temp = m
            hours = sum([math.ceil(float(p)/m) for p in piles])
            print(f'm: {m}, hours: {hours}, l: {l}, r: {r}')
            if hours > h:
                l = m + 1
            elif hours <= h: # meet the requirement, so we record the speed and shrink the search range
                k = m
                r = m - 1
        return k