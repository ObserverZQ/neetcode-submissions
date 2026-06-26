import heapq
from typing import List

'''
With tuples, Python will use the first element of the tuple as the priority.
If two tuples have the same first element, Python will compare the second element of the tuples, and so on.
'''
def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap = []
    res = []
    for num in nums:
        heapq.heappush(heap, (-num, num))
    while heap:
        res.append(heapq.heappop(heap)[1])
    return res


# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
