class Solution:
    '''
    Instead of just using a visited set, we maintain an array storing the best probability found so far for each node.
    This allows us to skip processing a node if we have already found a better path to it, reducing unnecessary work.
    '''
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = [[] for _ in range(n)]
        for i in range(len(edges)):
            src, dst = edges[i]
            adj[src].append((dst, succProb[i]))
            adj[dst].append((src, succProb[i]))

        maxProb = [0] * n
        maxProb[start_node] = 1.0
        pq = [(-1.0, start_node)]

        while pq:
            curr_prob, node = heapq.heappop(pq)
            curr_prob *= -1

            if node == end_node:
                return curr_prob
            if curr_prob < maxProb[node]:
                continue

            for nei, edge_prob in adj[node]:
                new_prob = curr_prob * edge_prob
                if new_prob > maxProb[nei]:
                    maxProb[nei] = new_prob
                    heapq.heappush(pq, (-new_prob, nei))

        return 0.0