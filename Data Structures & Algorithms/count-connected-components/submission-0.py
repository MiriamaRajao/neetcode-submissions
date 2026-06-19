class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # Form the adjacency list
        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Visited
        visited = set()

        # Perform dfs
        def dfs(node):
            if node in visited:
                return

            visited.add(node)

            for neighbor in graph[node]:
                dfs(neighbor)

        # Start from all the nodes
        # Counting connected
        connected = 0

        for i in range(n):
            if i not in visited:
                dfs(i)
                connected += 1

        return connected