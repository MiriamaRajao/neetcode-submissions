"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # It none
        if node is None:
            return None

        # Keep track of the old to new dict
        old_to_new = {}

        # Perform a dfs to explore the graph
        def dfs(original_node):

            # If we have already visited this node, just give the old_to_new value for that node
            if original_node in old_to_new:
                # Return the correspondig new node
                return old_to_new[original_node]

            # Otherwise process this node and add it to our old_to_new mapping
            cloned_node = Node(original_node.val)

            # Add to old_to_new visited dict
            old_to_new[original_node] = cloned_node

            # Dfs through the neighors and append it to the cloned node
            for neighbor in original_node.neighbors:
                cloned_neighbor = dfs(neighbor)
                cloned_node.neighbors.append(cloned_neighbor)

            # Then return the cloned node
            return cloned_node   

        # Return
        return dfs(node)      