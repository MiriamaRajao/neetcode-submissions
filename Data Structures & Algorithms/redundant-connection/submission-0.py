class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        # Set up the parents and the size arrays
        n = len(edges)
        parent = [i for i in range(n+1)]
        size = [1] * (n+1)

        # Define function to find parents
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x

        # Define function that checks and combine the groups
        def union(a, b):
            boss_a = find(a)
            boss_b = find(b)

            # Case for redundant chain
            if boss_a == boss_b:
                return False

            # Else group things, make the bigger group the parent
            if size[boss_a] < size[boss_b]:
                parent[boss_a] = boss_b
                size[boss_b] += size[boss_a]
            else:
                parent[boss_b] = boss_a
                size[boss_a] += size[boss_b]

            return True


        # Process each edge
        for a, b in edges:
            # Processing a, b, redundant edge is when a and b are already connected
            if not union(a, b):
                return [a, b]