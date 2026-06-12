class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        # 1. randomly push to maxheap
        heapq.heappush(self.maxHeap, -1 * num)

        # 2. check num properties of the heaps and swap if unmatched
        if self.maxHeap and self.minHeap and self.maxHeap[0] * -1 > self.minHeap[0]:
            heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, num)
        
        # 3. check heap sizes to make difference in height no more than 1
        if len(self.maxHeap) > len(self.minHeap) + 1:
            popped = -1 * heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, popped)
        elif len(self.minHeap) > len(self.maxHeap) + 1:
            popped = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -1 * popped)

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return self.maxHeap[0] * -1
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return (self.minHeap[0] + (self.maxHeap[0] * -1)) / 2