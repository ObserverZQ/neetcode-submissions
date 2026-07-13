class Solution:
    # time: O(nlogn), space: O(n)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        output = []

        for i in range(len(nums)):
            heapq.heappush(heap, (-nums[i], i))
            # when the window has at least k elements, we need to check if the current max is still in the window
            # if not, we pop the heap and add the smaller max which is still in the window to the res
            if i >= k - 1: 
                while heap[0][1] <= i - k: # the maximum is out of window
                    heapq.heappop(heap)
                output.append(-heap[0][0]) # notice we dont have to pop the max
        return output