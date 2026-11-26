class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # valid tree: 1. connected. start from a node and it can reach all nodes, meaning the nodes we have visited must match the total count 2. no cycle, meaning if we keep going to the connected nodes we won't see any node in the visited set
        adj = { i: [] for i in range(n)} # record neighbors for every node
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        visited = set()

        # the parent of the node, so we can skip it to avoid meaningless traveling
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)

            for nei in adj[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and len(visited) == n
