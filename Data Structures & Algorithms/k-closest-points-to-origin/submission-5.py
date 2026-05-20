class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean = lambda x: x[0] ** 2 + x[1] ** 2
        topk = heapq.nsmallest(k, points, key=lambda x: euclidean(x))
        return topk