import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # base case, only one stone remaining
        if len(stones) == 1:
            return stones[0]
        if len(stones) == 2:
            return abs(stones[1] - stones[0])
        # sort the stones in descending order, or create a max-heap(negate the values to use min-heap)
        # max_heap = [-x for x in stones]
        # heapq.heapify(max_heap)
        max_heap = stones[:]
        heapq.heapify_max(max_heap) # the _max postfix of API is supported on Python 3.14

        while len(max_heap) > 1:
            y = heapq.heappop_max(max_heap)
            x = heapq.heappop_max(max_heap)
            if y != x:
                diff = y - x
                heapq.heappush_max(max_heap, y - x)
        if len(max_heap) == 1:
            return heapq.heappop(max_heap)
        else:
            return 0


