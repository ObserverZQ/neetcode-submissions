class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []

        for time in times:
            u, v, t = time
            adj[u].append((v, t))
        
        shortest = {} # total cost
        src = k # starting node
        minHeap = [(0, src)] # top refers to min cost node
 
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            
            if n1 in shortest:
                continue
            
            shortest[n1] = w1
            
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minHeap, (w1 + w2, n2))

        print(f'shortest: {shortest}, { len(shortest.keys())}, {n}')
        return max(shortest.values()) if len(shortest.keys()) == n else -1

