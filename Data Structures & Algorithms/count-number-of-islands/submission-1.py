from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Grid geometry
        ROWS = len(grid)
        COLS = len(grid[0])

        # Directions definition
        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        visited = set()

        def dfs(i, j):
            # Out of bounds
            if i < 0 or i >= ROWS or j < 0 or j >= COLS:
                return

            # Water
            if grid[i][j] == "0":
                return

            # Already visited
            if (i, j) in visited:
                return

            # Mark land as visited
            visited.add((i, j))

            # Explore neighbors
            for dr, dc in directions:
                next_i = i + dr
                next_j = j + dc
                dfs(next_i, next_j)

        count = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    count += 1

        return count