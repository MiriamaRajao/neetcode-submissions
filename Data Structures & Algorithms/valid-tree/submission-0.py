class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Check if len(edges) is different from n - 1
        if len(edges) != n - 1:
            return False

        # Create adjacency list
        graph = {i: [] for i in range(n)}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Visited
        visited = set()

        # Check connectivity: If we can reach all other nodes from one node
        def dfs(node):
            # If node in visited
            if node in visited:
                return

            # Add this node to visited
            visited.add(node)

            # Look through neighbors
            for neighbor in graph[node]:
                dfs(neighbor)

        # Start from initial node
        dfs(0)

        return len(visited) == n