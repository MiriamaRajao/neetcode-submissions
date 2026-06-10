"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Edge case
        if not node:
            return None

        visited = {}

        # DFS function to traverse and clone the graph
        def dfs(node):
            if node in visited:
                return visited[node]

            # Create a clone and add it to the visited dictionary
            clone = Node(node.val)
            visited[node] = clone

            # Recursively clone neighbors
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone  # ✅ This line was missing

        return dfs(node)

# TC : O(n + e)
# SC : O(n + e)	
        