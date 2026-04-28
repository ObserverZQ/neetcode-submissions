class Solution:
    # bucket sort. use a list where the index represents the frequency
    # at each index we store the numbers that appear 'index' times in the input
    # time O(n), space O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        count = {}
        # notice we use n+1 in range to record number that appear n times
        freq = [[] for _ in range(n + 1)]
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(n, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res