class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # result = prob[i] * prob[j] * ... all with highest cost
        # so it is an opposite of min cost Dijkstra

        # 1. create the neighbors hashmap
        # adj = {}
        # for i in range(n): # 0-indexed so we iterate from 0 - 2
        #     adj[i] = []
        adj = collections.defaultdict(list)
        # print(zip(edges, succProb))
        for edge, p in zip(edges, succProb):
            s, e = edge
            adj[s].append((e, p))
            adj[e].append((s, p)) # it's an undirected graph so we need to work on the reverse direction as well

        maxHeap = [(-1, start_node)] # store the total probability of reaching each node in the graph
        visited = set()

        while maxHeap:
            p, node = heapq.heappop(maxHeap) # always pop the highest value in the heap
            visited.add(node)

            if node == end_node:
                return -p
            
            for nei, prob in adj[node]:
                if nei not in visited:
                    heapq.heappush(maxHeap, (p * prob, nei))
        
        return 0