class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # we can use a min heap to store tuples, the first in it store the freq, the second the actual number
        # by storing the freq in a heap of size K, we get the top K freq numbers, with the least frequent pair at the top
        # finally we pop all the elements and gather the second value
        pairs = []
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        # another way to get the key and values:
        # for num, f in freq.items()
        for num in freq:
            # print('num', num)
            heapq.heappush(pairs, (freq[num], num))
            # check size of the heap to save space
            # print('pairs', pairs)
            if len(pairs) > k:
                heapq.heappop(pairs)
                # print('after size exceeded, pairs', pairs)
        res = []
        while len(pairs):
            res.append(heapq.heappop(pairs)[1])
        return res