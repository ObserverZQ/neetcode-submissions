class Solution:
    # use a max-heap to run the most frequent task based on their number of occurence,
    # and a queue to store tasks bing cooled down
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Counter is a specialized dictionary subclass from the collections module
        # designed to count the occurrences of hashable objects.
        # It automatically tallies items from an iterable,
        # storing the items as keys and their counts as values.
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()] # each number represents a unique task's execution count
        heapq.heapify(maxHeap) # this is a min-heap. but with negative signs we have the max positive cnt at the top

        time = 0 # a stop watch
        q = deque() # a queue to store the [-cnt, readyTime]

        while maxHeap or q:
            time += 1

            # 1.check heap
            if not maxHeap: # we fast forward time to the latest readyTime in the queue
                time = q[0][1]
            else:
                # the maxHeap runs the top task and check its remaining cnt.
                cnt = 1 + heapq.heappop(maxHeap) # the heap store negative vals, so we add 1
                if cnt: # there are still identical tasks waiting to be run, so it needs cooling down
                    q.append([cnt, time + n])
            
            # 2. check cooldown queue
            if q and q[0][1] == time: # the readyTime is now, we pop the queue and put it in the maxHeap
                heapq.heappush(maxHeap, q.popleft()[0])
        return time