class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # I'd like to use heap, but I kinda forgot the api/grammar.
        # anyways, let's try and record what was missing.

        # create a heap of size K. have a set 
        # i got stuck in the algorithm idea.
        # i thought about using a map to record the frequency of each num

        # i also thought about sorting, so the same num would be stuck together in the sorted array. the problem is that the sorted array is not based on frequency. 
        # got the hint: using min heap with tuples, the first the freq, the second the num itself. so how do we update the freq? -- first do counting for the whole nums, then create a heap.
        countMap = defaultdict(int)
        for num in nums:
            countMap[num] += 1
        # now that we have num as key and freq as value. we create a min heap with freq at the front.
        heap = []
        # res = []
        for num, freq in countMap.items():
            heapq.heappush(heap, (freq, num))
            # print(n, freq)
        topK = heapq.nlargest(k, heap)
        # print([n for _, n in topK])
        return [n for _, n in topK]

